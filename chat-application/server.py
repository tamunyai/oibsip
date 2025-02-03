import socket
import threading

from config import HOST, PORT

clients = {}  # Stores {socket: username}


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
        clients[client_socket] = username
        print(f"[NEW USER] {username} joined the chat.")

        broadcast(f"{username} has joined the chat!", client_socket)

        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break

            broadcast(f"> [{username}]: {message}", client_socket)

    except:
        pass

    finally:
        username = clients.pop(client_socket, "Unknown")
        broadcast(f"{username} has left the chat.", client_socket)
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
