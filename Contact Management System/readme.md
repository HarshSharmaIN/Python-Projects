Contact Management System Manual 

 

1. Introduction 

The Contact Management System is a simple yet effective application designed to help you manage your contacts. It allows you to add, edit, search, and delete contact entries. The system is user-friendly and provides feedback through a graphical user interface. 

 

2. Installation and Setup 

Before using the Contact Management System, make sure you have the necessary software and database set up. 

 

   Python: You need Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/). 

 

   MySQL Database: You should have a MySQL database server set up. Ensure you have a database named "abhay" with the user "root" and the password "abhay" as specified in the code. If needed, modify the code to match your database configuration. 

 

   Required Libraries: You need to have the required Python libraries installed. You can install them using pip: 

 

     ``` 

     pip install mysql-connector-python tkinter pillow 

     ``` 

 

3. User Interface Overview 

When you run the application, a graphical user interface (GUI) window will appear. It contains several frames for different contact management operations: 

 

   Add Frame: This is the default frame where you can add a new contact. 

 

   Edit Frame: Use this frame to edit an existing contact. 

 

   Search Frame: Here, you can search for contacts by first name or phone number. 

 

   Delete Frame: This frame allows you to delete a contact based on criteria. 

 

   Status Bar: At the bottom, there is a status bar that displays messages or the status of operations. 

 

   Buttons: Each frame contains buttons for performing actions such as adding, editing, searching, and deleting contacts. 

 

4. Adding a New Contact 

To add a new contact, follow these steps: 

           a. Open the application, and you will be on the "Add Contact" frame. 

           b. Fill in the contact details in the respective fields: 

         - First Name 

      - Last Name 

      - Address 

      - Phone Number 

      - Email 

 

     c. Click the "Add Contact" button. The system will add the contact to the database and display a success message or an error message if something goes wrong. 

 

   d. You can use the "Clear Fields" button to clear the input fields for the next contact entry. 

 

5. Editing an Existing Contact 

To edit an existing contact, follow these steps: 

 

   a. Click the "Edit Contact" button on the "Add Contact" frame. 

 

   b. Enter the phone number of the contact you want to edit and the new contact details (first name, last name, address, email). 

 

   c. Click the "Edit Contact" button. The system will update the contact in the database and display a success message or an error message if no matching contact is found. 

 

   d. You can click the "Back" button to return to the "Add Contact" frame. 

 

6. Searching for Contacts 

To search for contacts, follow these steps: 

 

   a. Click the "Search Contact" button on the "Add Contact" frame. 

 

   b. Enter the search criteria (either first name or phone number) in the input field. 

 

   c. Click the "Search Contact" button. The system will display the contact details if a matching contact is found or a message if no contact matches the criteria. 

 

   d. You can click the "Back" button to return to the "Add Contact" frame. 

 

7. Deleting a Contact 

To delete a contact, follow these steps: 

 

   a. Click the "Delete Contact" button on the "Add Contact" frame. 

 

   b. Choose a delete option (1 for first name, 2 for phone number) and enter the criteria. 

 

   c. Click the "Delete Contact" button. The system will delete the contact from the database and display a success message or an error message if no matching contact is found. 

 

   d. You can click the "Back" button to return to the "Add Contact" frame. 

 

8. Viewing All Contacts 

To view all contacts in the database, follow these steps: 

 

   a. Click the "View All Contacts" button on the "Add Contact" frame. 

 

   b. The system will display a message box with a list of all contacts, including their first name, last name, address, phone number, and email. 

 

9. Additional Tips and Information 

   - If you encounter any errors or need assistance, the status bar at the bottom of the application will provide feedback and guidance. 

 

   - Ensure that the information you enter is accurate, especially when adding or editing contacts, as this system does not perform extensive validation. 

 

   - Remember to maintain backups of your database to prevent data loss. 

 

   - You can customize the code further to match your specific requirements, such as modifying the database configuration or adding more fields to the contact table. 

 

This manual should help you get started with the Contact Management System. Enjoy managing your contacts efficiently using this simple, user-friendly application. 

 

 

Working 

 

1. Database Connection and Table Creation: 

   - The program starts by establishing a connection to a MySQL database. It connects to a database named "abhay" with the username "root" and password "abhay." 

   - It then checks if a table named "contactbook" exists in the database. If it doesn't exist, the program creates this table with columns for contact information, such as first name, last name, address, phone number, and email. 

 

2. Adding a New Contact (`add_contact` function): 

   - To add a new contact, you need to provide details including the first name, last name, address, phone number, and email in the GUI. 

   - The program first validates that the provided phone number is a valid number. 

   - It then checks if a contact with the same phone number already exists in the database. If it does, it displays an error message. 

   - If the contact is unique, the program inserts the new contact information into the database, and a success message is shown to the user. 

 

3. Editing an Existing Contact (`edit_contact` function): 

   - To edit an existing contact, you need to provide the phone number of the contact you want to modify and the updated contact information. 

   - The program first validates the phone number. 

   - It then updates the contact information in the database for the specified phone number. If no matching contact is found, an error message is displayed. 

 

4. Searching for Contacts (`search_contact` function): 

   - You can search for contacts by either first name or phone number. 

   - The program performs a database query based on the provided search criteria (first name or phone number). 

   - If a contact matching the criteria is found, the program displays the contact details. If no contact matches the criteria, it shows a message indicating that the contact was not found. 

 

5. Deleting a Contact (`delete_contact` function): 

   - To delete a contact, you need to specify the criteria for deletion (either by first name or phone number) and the actual criteria value. 

   - The program constructs a SQL query based on the delete option and criteria, then executes it to delete the contact. 

   - If the contact is successfully deleted, a success message is displayed. If no matching contact is found, an error message is shown. 

 

6. Viewing All Contacts (`view_contacts` function): 

   - This function retrieves all contacts from the database and displays them. 

   - If there are contacts, the program lists them in a message box. If there are no contacts, it displays a message indicating that no contacts were found. 

 

7. User Interface and Frame Management: 

   - The program creates a graphical user interface with different frames for each contact management operation (add, edit, search, delete). 

   - Users can switch between frames to perform different operations. 

   - Entry fields, labels, buttons, and a status bar are provided to facilitate user interaction and feedback. 

 

8. Status Bar (`update_status` function): 

   - The status bar at the bottom of the GUI is used to display messages and the status of operations. 

   - The `update_status` function updates the text displayed in the status bar based on the operation's outcome. 

 

9. Clearing Input Fields (`clear_fields` function): 

   - The `clear_fields` function is used to clear input fields when needed, making it easier for users to add or edit new contacts. 

 

10. Main Loop: 

    - The program enters the tkinter main event loop (`root.mainloop()`), which is responsible for keeping the GUI responsive and handling user interactions. 

 

Function of thinkter 

 

1. tk.Tk(): 

   - This function initializes the main application window and is typically the first function called when creating a tkinter GUI. 

   - It creates the main application window, which is often referred to as `root`. 

   - In the code, `root` is the main window for the Contact Management System. 

 

2. Label: 

   - The `Label` widget is used to display static text or images on the GUI. 

   - It is created using the `Label` constructor, and you can specify the parent frame and the text or image to be displayed. 

   - In the code, labels are used to display text such as "First Name," "Last Name," etc. 

 

3. Entry: 

   - The `Entry` widget is an input field where users can type text or numbers. 

   - It is created using the `Entry` constructor and is often associated with labels to indicate the purpose of the input. 

   - In the code, entry fields are used for users to enter contact information. 

 

4. Button: 

   - The `Button` widget is used to create clickable buttons that perform specific actions when pressed. 

   - It is created using the `Button` constructor and can be associated with a function to execute when clicked. 

   - In the code, buttons are used for actions like adding contacts, editing, searching, and more. 

 

5. Frame: 

   - The `Frame` widget is used to create container widgets that can hold other widgets. 

   - It helps organize and group related widgets together within a window. 

   - In the code, frames are used for separating different sections of the application, such as the add, edit, search, and delete sections. 

 

6. `ttk` (Themed Tkinter) Module: 

   - The `ttk` module provides improved and themed versions of some widgets. 

   - The `ttk.Button` is used in the code to create styled buttons. 

 

7. `messagebox` Module: 

   - The `messagebox` module provides functions to create popup message boxes for displaying information or errors to the user. 

   - It's used to show informative or error messages when certain actions are taken in the application. 

 

8. `StringVar` and `TextVar`: 

   - `StringVar` and `TextVar` are variables used to store and manipulate text and string data. 

   - They can be associated with widgets like labels, entry fields, and status bars to display and update dynamic text content. 

 

9. `grid` Geometry Manager: 

   - The `grid` geometry manager is used to arrange widgets in a grid layout, similar to a table with rows and columns. 

   - It allows you to specify the row and column positions of widgets and their placement within the grid. 

 

10. `pack` and `place` Geometry Managers: 

    - While the code primarily uses the `grid` geometry manager, tkinter also provides `pack` and `place` for alternative ways to manage widget placement within a window. 

 

11. `bind` Method: 

    - The `bind` method is used to bind events to functions. It allows you to specify an event (e.g., button click) and the function to execute when that event occurs. 

 

12. `update_status` Function: 

    - This is a custom function in the code that updates the text displayed in the status bar at the bottom of the GUI. 

    - It uses a `StringVar` to dynamically update the status message. 

 

13. `show_frame` Function: 

    - Another custom function in the code, it is used to switch between frames (add, edit, search, delete). 

    - It controls which frame is displayed in the GUI based on user actions. 

 

14. `mainloop` Method: 

    - The `mainloop` method is used to start the tkinter main event loop. 

    - It keeps the GUI responsive and handles user interactions, such as button clicks and other events. 

 

These are some of the primary functions and components of the `tkinter` library used in the Contact Management System code. They help create the GUI and enable user interaction with the application. 

 

 

Summary of the Contact Management System: 

 

The Contact Management System is a Python application with a graphical user interface (GUI) built using the `tkinter` library. This system allows users to manage a list of contacts by performing various operations such as adding, editing, searching, and deleting contact entries in a MySQL database. Here's a brief summary of its key features and functionality: 

 

Key Features: 

 

1. Add New Contacts: Users can add new contact information, including first name, last name, address, phone number, and email. The system performs input validation to ensure data accuracy. 

 

2. Edit Existing Contacts: Existing contacts can be edited by providing the phone number of the contact to be modified and updating the contact information. 

 

3. Search Contacts: Users can search for contacts based on either the first name or phone number. The system displays the contact details if a match is found. 

 

4. Delete Contacts: Contacts can be deleted based on criteria (either first name or phone number). The system executes the deletion and provides feedback to the user. 

 

5. View All Contacts: The system can display a list of all contacts stored in the database, including their details such as first name, last name, address, phone number, and email. 

 

6. User-Friendly Interface: The GUI provides a user-friendly and intuitive experience, with frames for different operations, input fields, labels, buttons, and a status bar for displaying messages. 

 

How It Works: 

 

- The system connects to a MySQL database and creates a "contactbook" table to store contact information. 

- Users interact with the GUI, selecting the desired operation (add, edit, search, delete) by switching between frames. 

- Input fields and labels guide users in entering and understanding contact information. 

- The status bar provides real-time feedback, displaying success messages or error messages for each operation. 

- The system employs input validation to ensure data integrity and handles edge cases, such as checking for existing contacts with the same phone number before adding new ones. 

 

Additional Information: 

 

- The code can be customized to match specific database configurations or additional contact fields. 

- Users are encouraged to maintain database backups to prevent data loss. 

 

Overall, the Contact Management System is a simple yet effective tool for efficiently managing a list of contacts. It provides a user-friendly interface and clear feedback to assist users in adding, editing, searching, and deleting contacts with ease. 