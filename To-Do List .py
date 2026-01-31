# To-Do List

# Initialize an empty list to store tasks
tasks = []

# Infinite loop to keep the program running until the user exits
while True:
    # Display menu options to the user
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Task")
    print("4. Exit")

    # Take user input for the command and convert it to lowercase
    user_command = input("Enter Command: ").lower()

    # Correct way is: 'user_command == "1" or user_command == "add task"'
    if user_command == "1" or user_command == "add task":
        # Ask the user for the task to add
        task_to_add = input("Enter Task To Add: ")
        # Confirm addition
        confirm = input("Confirm(y/n): ").lower()

        # If user confirms, add the task to the list
        if confirm == "y" or confirm == "yes":
            tasks.append(task_to_add)
            print(f"Task Added: {task_to_add}")
        else:
            continue  # Skip to the next loop iteration if user cancels

    # Remove Task option
    elif user_command == "2" or user_command == "remove task":
        # Check if there are tasks to remove
        if len(tasks) == 0:
            print("No Tasks To Remove")
            continue  # Go back to start of loop

        # Ask the user for the task number to remove (1-based index)
        task_to_remove = int(input("Enter Task Number To Remove: ")) - 1
        # Confirm removal
        confirm = input("Confirm(y/n): ").lower()

        # If confirmed, remove the task from the list
        if confirm == "y" or confirm == "yes":
            tasks.pop(task_to_remove)
            print(f"Task Removed: {task_to_remove}")
        else:
            continue

    # View Task option
    elif user_command == "3" or user_command == "view task":
        if len(tasks) > 0:
            # Enumerate tasks to display them with numbering
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No Tasks Available")

    # Exit option
    elif user_command == "4" or user_command == "exit":
        print("Bye!")
        break  # Exit the loop and end the program
