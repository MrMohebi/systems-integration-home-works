import socket

from  guessWord import WordGuess


def server_program():
    host = socket.gethostname()
    port = 5007  # initiate port no above 1024
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(2)
        conn, addr = server_socket.accept()
        with conn:
            print("Connection from: " + str(addr))
            game = WordGuess()
            conn.send(game.show_current_state().encode())
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                is_finished = play_guess_word_game(conn, game, data)
                if is_finished:
                    break


def play_guess_word_game(conn, game, inp):
    result = game.play_game(inp)
    conn.send(result.encode())
    state = game.show_current_state()
    conn.send(state.encode())
    return game.is_finish

if __name__ == '__main__':
    server_program()