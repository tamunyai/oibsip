import socket
import threading
import random

from config import HOST, PORT

clients = {}  # Stores {socket: username}

colors = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
]

def broadcast(message, sender_socket):
    for client, _ in clients.items():
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except:
                client.close()
                del client


def handle_client(client_socket):
    try:
        username = client_socket.recv(1024).decode("utf-8")
        color = random.choice(colors)
        colored_username = f"{color}{username}\033[0m"

        clients[client_socket] = (username, color)
        client_socket.send(colored_username.encode("utf-8"))

        print(f"[NEW USER] {username} joined the chat.")

        broadcast(f"{colored_username} has joined the chat!", client_socket)

        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break

            broadcast(f"> [{colored_username}]: {message}", client_socket)

    except:
        pass

    finally:
        username, _ = clients.pop(client_socket, ("Unknown", ""))
        broadcast(f"{colored_username} has left the chat.", client_socket)
        client_socket.close()
        print(f"[DISCONNECTED] {username} left.")


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

    while True:
        client_socket, _ = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


if __name__ == "__main__":
    start_server()
