import socket

word_dic = ['apple', 'banana', 'orange', 'grape', 'peach', 'kiwi']


def find_word(letter):
    global word_dic
    result_list = [word for word in word_dic if word.startswith(letter)]
    if len(result_list) < 1:
        return "NO WORD FOUNDED!"
    return result_list[0]

def server_program():
    host = socket.gethostname()
    port = 5007  # initiate port no above 1024
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(2)
        conn, addr = server_socket.accept()
        with conn:
            print("Connection from: " + str(addr))
            conn.send("let's play :)".encode())
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                conn.send(find_word(data[-1]).encode())


if __name__ == '__main__':
    server_program()