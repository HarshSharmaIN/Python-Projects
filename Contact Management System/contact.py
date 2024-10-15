import mysql.connector as sql
import tkinter as tk
from tkinter import ttk, messagebox


# Initialize the MySQL database connection
my = sql.connect(host="localhost", user="root", password="abhay", database="abhay")
cursor = my.cursor()

# Create the 'contactbook' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contactbook (
        fname varchar(50) primary key, 
        lname varchar(50), 
        address varchar(100),
        number numeric(12) primary key,
        email varchar(20)
    )
''')

# Function to add a contact to the database
def add_contact():
    fname = entry_fname.get()
    lname = entry_lname.get()
    address = entry_address.get()
    number = entry_number.get()
    email = entry_email.get()
    
    if fname and lname and number:
        try:
            number = int(number)
        except ValueError:
            messagebox.showerror("Add Contact", "Phone Number must be a valid number")
            return

        cursor.execute("SELECT * FROM contactbook WHERE number = %s", (number,))
        existing_contact = cursor.fetchone()

        if existing_contact:
            messagebox.showerror("Add Contact", "Contact already exists with the same Phone Number.")
        else:
            query = "INSERT INTO contactbook (fname, lname, address, number, email) VALUES (%s, %s, %s, %s, %s)"
            values = (fname, lname, address, number, email)
            cursor.execute(query, values)
            my.commit()
            update_status("Contact added successfully")
    else:
        messagebox.showerror("Add Contact", "First Name, Last Name, and Phone Number are required")

# Function to edit a contact in the database
def edit_contact():
    number = entry_edit_number.get()
    new_fname = entry_fname.get()
    new_lname = entry_lname.get()
    new_address = entry_address.get()
    new_email = entry_email.get()
    
    if number and (new_fname or new_lname):
        try:
            number = int(number)
        except ValueError:
            messagebox.showerror("Edit Contact", "Phone Number must be a valid number")
            return

        query_number = "UPDATE contactbook SET fname = %s, lname = %s, address = %s, email = %s WHERE number = %s"
        values_number = (new_fname, new_lname, new_address, new_email, number)
        cursor.execute(query_number, values_number)
        my.commit()

        if cursor.rowcount > 0:
            update_status("Contact updated successfully")
        else:
            update_status("No matching contact found for editing")
    else:
        messagebox.showerror("Edit Contact", "Phone Number and First Name/Last Name are required")

# Function to search for a contact in the database
def search_contact():
    search_criteria = entry_search.get()
    if search_criteria:
        query = "SELECT * FROM contactbook WHERE fname = %s OR number = %s"
        cursor.execute(query, (search_criteria, search_criteria))
        result = cursor.fetchall()

        if result:
            result_text = "\n".join([f"First Name: {row[0]}, Last Name: {row[1]}, Address: {row[2]}, Phone Number: {row[3]}, Email: {row[4]}" for row in result])
            messagebox.showinfo("Search Result", f"Contact details:\n{result_text}")
        else:
            messagebox.showinfo("Search Result", "Contact not found")
    else:
        messagebox.showerror("Search Contact", "Please enter a search criteria")

# Function to delete a contact from the database
def delete_contact():
    delete_option = entry_delete_option.get()
    delete_criteria = entry_delete.get()
    
    if delete_option and delete_criteria:
        query = "DELETE FROM contactbook WHERE "
        if delete_option == '1':
            query += "fname = %s"
        elif delete_option == '2':
            query += "number = %s"
        cursor.execute(query, (delete_criteria,))
        my.commit()
        
        if cursor.rowcount > 0:
            update_status("Contact deleted successfully")
        else:
            update_status("No matching contact found for deletion")
    else:
        messagebox.showerror("Delete Contact", "Delete Option and Criteria are required")

# Function to fetch and display all contacts from the database
def view_contacts():
    cursor.execute("SELECT * FROM contactbook")
    contacts = cursor.fetchall()

    if contacts:
        result_text = "\n".join([f"First Name: {row[0]}, Last Name: {row[1]}, Address: {row[2]}, Phone Number: {row[3]}, Email: {row[4]}" for row in contacts])
        messagebox.showinfo("All Contacts", f"List of Contacts:\n{result_text}")
    else:
        messagebox.showinfo("All Contacts", "No contacts found.")

# Create the main GUI window
root = tk.Tk()
root.title("Contactbook")



# Create frames for each operation
add_frame = tk.Frame(root)
edit_frame = tk.Frame(root)
search_frame = tk.Frame(root)
delete_frame = tk.Frame(root)

# Function to switch between frames
def show_frame(frame):
    frame.tkraise()

# Configure frames
for frame in (add_frame, edit_frame, search_frame, delete_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# Create and configure widgets for adding a contact
label_fname = tk.Label(add_frame, text="First Name:")
entry_fname = tk.Entry(add_frame)
label_lname = tk.Label(add_frame, text="Last Name:")
entry_lname = tk.Entry(add_frame)
label_address = tk.Label(add_frame, text="Address:")
entry_address = tk.Entry(add_frame)
label_number = tk.Label(add_frame, text="Phone Number:")
entry_number = tk.Entry(add_frame)
label_email = tk.Label(add_frame, text="E-mail:")
entry_email = tk.Entry(add_frame)
button_add = ttk.Button(add_frame, text="Add Contact", command=add_contact)
button_show_edit = ttk.Button(add_frame, text="Edit Contact", command=lambda: show_frame(edit_frame))
button_show_search = ttk.Button(add_frame, text="Search Contact", command=lambda: show_frame(search_frame))
button_show_delete = ttk.Button(add_frame, text="Delete Contact", command=lambda: show_frame(delete_frame))
button_view = ttk.Button(add_frame, text="View All Contacts", command=view_contacts)
button_clear_fields = ttk.Button(add_frame, text="Clear Fields", command=lambda: clear_fields(entry_fname, entry_lname, entry_address, entry_number, entry_email))

# Use the grid manager for widgets in add_frame
label_fname.grid(row=0, column=0, sticky='w')
entry_fname.grid(row=0, column=1)
label_lname.grid(row=1, column=0, sticky='w')
entry_lname.grid(row=1, column=1)
label_address.grid(row=2, column=0, sticky='w')
entry_address.grid(row=2, column=1)
label_number.grid(row=3, column=0, sticky='w')
entry_number.grid(row=3, column=1)
label_email.grid(row=4, column=0, sticky='w')
entry_email.grid(row=4, column=1)
button_add.grid(row=5, columnspan=2, pady=10)
button_show_edit.grid(row=6, column=0, pady=5)
button_show_search.grid(row=6, column=1, pady=5)
button_show_delete.grid(row=7, columnspan=2, pady=5)
button_view.grid(row=8, columnspan=2, pady=10)
button_clear_fields.grid(row=9, columnspan=2, pady=10)

# Create and configure widgets for editing a contact
label_edit_number = tk.Label(edit_frame, text="Edit - Phone Number:")
entry_edit_number = tk.Entry(edit_frame)
button_edit = ttk.Button(edit_frame, text="Edit Contact", command=edit_contact)
button_back_edit = ttk.Button(edit_frame, text="Back", command=lambda: show_frame(add_frame))

# Use the grid manager for widgets in edit_frame
label_edit_number.grid(row=0, column=0, sticky='w')
entry_edit_number.grid(row=0, column=1)
button_edit.grid(row=1, column=0, columnspan=2, pady=5)
button_back_edit.grid(row=2, column=0, columnspan=2, pady=5)

# Create and configure widgets for searching a contact
label_search = tk.Label(search_frame, text="Search by First Name or Phone Number:")
entry_search = tk.Entry(search_frame)
button_search = ttk.Button(search_frame, text="Search Contact", command=search_contact)
button_back_search = ttk.Button(search_frame, text="Back", command=lambda: show_frame(add_frame))

# Use the grid manager for widgets in search_frame
label_search.grid(row=0, column=0, sticky='w')
entry_search.grid(row=0, column=1)
button_search.grid(row=1, column=0, columnspan=2, pady=5)
button_back_search.grid(row=2, column=0, columnspan=2, pady=5)

# Create and configure widgets for deleting a contact
label_delete_option = tk.Label(delete_frame, text="Delete Option (1 for First Name, 2 for Phone Number):")
entry_delete_option = tk.Entry(delete_frame)
label_delete = tk.Label(delete_frame, text="Delete Criteria:")
entry_delete = tk.Entry(delete_frame)
button_delete = ttk.Button(delete_frame, text="Delete Contact", command=delete_contact)
button_back_delete = ttk.Button(delete_frame, text="Back", command=lambda: show_frame(add_frame))

# Use the grid manager for widgets in delete_frame
label_delete_option.grid(row=0, column=0, sticky='w')
entry_delete_option.grid(row=0, column=1)
label_delete.grid(row=1, column=0, sticky='w')
entry_delete.grid(row=1, column=1)
button_delete.grid(row=2, column=0, columnspan=2, pady=5)
button_back_delete.grid(row=3, column=0, columnspan=2, pady=5)

# Create a status bar
status_var = tk.StringVar()
status_bar = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.grid(row=1, column=0, columnspan=3, sticky="we")

# Function to update the status bar
def update_status(message):
    status_var.set(message)

# Function to clear input fields
def clear_fields(*entries):
    for entry in entries:
        entry.delete(0, 'end')

# Start the GUI main loop
show_frame(add_frame)
root.mainloop()