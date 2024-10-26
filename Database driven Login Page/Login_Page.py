import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import messagebox

def init_db():
   conn = sqlite3.connect('users.db')
   cursor = conn.cursor()
   cursor.execute('''
       CREATE TABLE IF NOT EXISTS users (
           id INTEGER PRIMARY KEY,
           username TEXT UNIQUE NOT NULL,
           password TEXT NOT NULL
       )
   ''')
   conn.commit()
   conn.close()

def add_user(username, password):
   conn = sqlite3.connect('users.db')
   cursor = conn.cursor()
   try:
       cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
       conn.commit()
       messagebox.showinfo("Success", f"User '{username}' added successfully.")
   except sqlite3.IntegrityError:
       messagebox.showerror("Error", f"User '{username}' already exists.")
   finally:
       conn.close()

def check_credentials(username, password):
   conn = sqlite3.connect('users.db')
   df = pd.read_sql_query('SELECT * FROM users', conn)
   conn.close()
   user = df[(df['username'] == username) & (df['password'] == password)]
   return not user.empty

def get_users():
   conn = sqlite3.connect('users.db')
   df = pd.read_sql_query('SELECT * FROM users', conn)
   conn.close()
   return df

def clear_all_users():
   conn = sqlite3.connect('users.db')
   cursor = conn.cursor()
   cursor.execute('DELETE FROM users')
   conn.commit()
   conn.close()

class UserApp:
   def __init__(self, master):
       self.master = master
       master.title("User Management System")
       master.geometry("600x750")  
       master.configure(bg="black")  

       self.title_label = tk.Label(master, text="User Management", font=("Consolas", 30, "bold"), bg="black", fg="green")
       self.title_label.pack(pady=30)

       self.label_username = tk.Label(master, text="Username", bg="black", fg="green", font=("Consolas", 20))
       self.label_username.pack(pady=15)
       self.entry_username = tk.Entry(master, width=60, font=("Consolas", 20), bg="black", fg="green", insertbackground='green')
       self.entry_username.pack(pady=10)

       self.label_password = tk.Label(master, text="Password", bg="black", fg="green", font=("Consolas", 20))
       self.label_password.pack(pady=15)
       self.entry_password = tk.Entry(master, show="*", width=60, font=("Consolas", 20), bg="black", fg="green", insertbackground='green')
       self.entry_password.pack(pady=10)

       self.button_frame = tk.Frame(master, bg="black")
       self.button_frame.pack(pady=30)

       self.button_login = tk.Button(self.button_frame, text="Login", command=self.login, width=20, bg="green", fg="black", font=("Consolas", 16))
       self.button_login.grid(row=0, column=0, padx=10)

       self.button_register = tk.Button(self.button_frame, text="Register", command=self.register, width=20, bg="green", fg="black", font=("Consolas", 16))
       self.button_register.grid(row=0, column=1, padx=10)

       self.button_view = tk.Button(master, text="View Users", command=self.view_users, width=25, bg="green", fg="black", font=("Consolas", 16))
       self.button_view.pack(pady=15)

       self.button_clear = tk.Button(master, text="Clear Users", command=self.clear_users, width=25, bg="green", fg="black", font=("Consolas", 16))
       self.button_clear.pack(pady=15)

   def login(self):
       username = self.entry_username.get()
       password = self.entry_password.get()
       if check_credentials(username, password):
           messagebox.showinfo("Login", "Login successful!")
       else:
           messagebox.showerror("Login", "Invalid username or password.")

   def register(self):
       username = self.entry_username.get()
       password = self.entry_password.get()
       if username and password:
           add_user(username, password)
       else:
           messagebox.showerror("Registration", "Please enter both username and password.")

   def view_users(self):
       users = get_users()
       if users.empty:
           messagebox.showinfo("Users", "No users found.")
       else:
           users_list = "\n".join(users['username'].tolist())
           messagebox.showinfo("Users", f"Registered Users:\n{users_list}")

   def clear_users(self):
       if messagebox.askyesno("Confirm", "Are you sure you want to clear all users?"):
           clear_all_users()
           messagebox.showinfo("Clear Users", "All users cleared.")

if __name__ == "__main__":
   init_db()
   root = tk.Tk()
   app = UserApp(root)
   root.mainloop()
