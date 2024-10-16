import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

HOST = 'localhost'  # Localhost
PORT = 65433        # Port number for the server

class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Client")

        self.chat_area = scrolledtext.ScrolledText(root, state='disabled')
        self.chat_area.pack(padx=10, pady=10)

        self.message_entry = tk.Entry(root)
        self.message_entry.pack(padx=10, pady=10, fill=tk.X)
        self.message_entry.bind("<Return>", self.send_message)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((HOST, PORT))
            self.update_chat_area("Connected to the server.")
            threading.Thread(target=self.receive_messages, daemon=True).start()
        except socket.error as e:
            self.update_chat_area(f"Connection error: {e}")
            self.root.quit()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.update_chat_area(message)
            except socket.error as e:
                self.update_chat_area(f"Socket error: {e}")
                break
        self.client_socket.close()

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            try:
                self.client_socket.send(message.encode('utf-8'))
                self.update_chat_area(f"You: {message}")
                self.message_entry.delete(0, tk.END)
            except socket.error as e:
                self.update_chat_area(f"Socket error: {e}")

    def update_chat_area(self, message):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, message + '\n')
        self.chat_area.configure(state='disabled')
        self.chat_area.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()
