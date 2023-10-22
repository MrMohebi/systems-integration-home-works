import random
import socket
import pickle

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(5)

client_socket, addr = server_socket.accept()
print(f"Connection from {addr} has been established!")

# Game Logic
board = [' ' for _ in range(9)]


def get_random_space_index(arr):
    space_indices = [i for i in range(len(arr)) if arr[i] == " "]
    if space_indices:
        return random.choice(space_indices)
    else:
        return None


def check_win(board, player):
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                        [0, 4, 8], [2, 4, 6]]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def check_board_full(board):
    return all(x != ' ' for x in board)


def send_data(data):
    client_socket.send(pickle.dumps(data))


def receive_data():
    return pickle.loads(client_socket.recv(1024))


def display_board(board):
    print("-------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("-------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("-------------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-------------")


def check_win(board, player):
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                        [0, 4, 8], [2, 4, 6]]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


while True:
    try:
        display_board(board)

        if check_board_full(board):
            data_to_send = {"board": board, "message": "Bord is full :(. its done."}
            send_data(data_to_send)

        random_space_index = get_random_space_index(board)
        board[get_random_space_index(board)] = "X"

        data_to_send = {"board": board, "message": "I'm (X), I'll go first..."}
        send_data(data_to_send)

        received_data = receive_data()
        print(f"Received data from client: {received_data}")

        break

    except Exception as e:
        print(f"An error occurred: {e}")
        break

client_socket.close()
server_socket.close()
