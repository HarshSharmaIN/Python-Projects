# Simple To-Do List Application

# Initialize an empty list to store tasks
todo_list = []

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"'{task}' has been added to your to-do list.")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def remove_task():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        view_tasks()
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            removed_task = todo_list.pop(task_num - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        except (ValueError, IndexError):
            print("Invalid task number!")

def todo_list_app():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1/2/3/4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    todo_list_app()

