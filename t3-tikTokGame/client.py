import socket
import pickle

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))


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


# Main game loop
while True:
    try:
        received_data = receive_data()
        if received_data["message"]:
            print(received_data["message"])
        board = received_data["board"]
        display_board(board)
        # Code for the game goes here
        # ...

        # Example: Sending and receiving data
        data_to_send = {"message": "Hello from client!"}
        send_data(data_to_send)

        # Break the loop condition based on your game logic
        break

    except Exception as e:
        print(f"An error occurred: {e}")
        break

# Close the connection
client_socket.close()
