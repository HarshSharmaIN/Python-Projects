import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

HOST = '192.168.29.224'  # Bind to all network interfaces
PORT = 65433      # Port number for the server

class ChatServer:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Server")

        # Create GUI components
        self.chat_area = scrolledtext.ScrolledText(root, state='disabled')
        self.chat_area.pack(padx=10, pady=10)

        self.message_entry = tk.Entry(root)
        self.message_entry.pack(padx=10, pady=10, fill=tk.X)
        self.message_entry.bind("<Return>", self.send_message)

        # Initialize the server
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen()
        self.clients = []  # List of client sockets
        self.update_chat_area("Server started, waiting for connections...")

        # Start accepting connections
        threading.Thread(target=self.accept_connections, daemon=True).start()

    def accept_connections(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.update_chat_area(f"Connection from {client_address}")
            self.clients.append(client_socket)
            # Start handling this client
            threading.Thread(target=self.handle_client, args=(client_socket,), daemon=True).start()

    def handle_client(self, client_socket):
        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.broadcast(f"Client: {message}", client_socket)
        except socket.error as e:
            self.update_chat_area(f"Socket error: {e}")
        finally:
            client_socket.close()
            self.clients.remove(client_socket)

    def broadcast(self, message, sender_socket):
        self.update_chat_area(message)
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except socket.error as e:
                    self.update_chat_area(f"Socket error: {e}")
                    client.close()
                    self.clients.remove(client)

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            self.broadcast(f"Server: {message}", None)
            self.message_entry.delete(0, tk.END)

    def update_chat_area(self, message):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, message + '\n')
        self.chat_area.configure(state='disabled')
        self.chat_area.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    server = ChatServer(root)
    root.mainloop()
