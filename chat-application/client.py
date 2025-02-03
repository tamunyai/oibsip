import socket
import threading

from config import HOST, PORT


def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break

            print(f"\r{message}")
            print(f"> : ", end="", flush=True)

    except:
        pass

    finally:
        client_socket.close()


def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    username = input("Enter your username: ")
    client_socket.send(username.encode("utf-8"))

    colored_username = client_socket.recv(1024).decode("utf-8")
    
    print(f"\nWelcome {colored_username}! You are now connected to the chat.")

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        message = input("> : ")
        if message.lower() == "exit":
            break

        client_socket.send(message.encode("utf-8"))

    client_socket.close()


if __name__ == "__main__":
    connect_to_server()
