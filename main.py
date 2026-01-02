# Main program
user_input = "Type add, show, edit, complete or exit: "
file_path = "todos.txt"
# todos = load_todos_from_file(file_path)  # Load todos at startup
file = open("todos.txt", "r")
todos = file.readlines()
file.close()
print(todos)
while True:
    user_response = input(user_input).strip()

    if "show" in user_response or "display" in user_response:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        if todos:
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item.strip('\n')}")
        else:
            print("No todos to display.")

    if "add" in user_response:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        if len(user_response) > 3:
            user_response = user_response[4:] + "\n"
        else:
            user_response = input("Enter new todo: ") + "\n"
        todos.append(user_response)
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    if "edit" in user_response:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        if todos:
            print("Which todo would you like to change?")
            for index, todo in enumerate(todos, start=1):  # Display todos with 1-based indexing
                print(f"{index}. {todo.strip('\n')}")

            this_one = input(f"Enter the number of the todo to change (1-{len(todos)}): ")

            # Validate the input
            if this_one.isdigit():
                this_one = int(this_one)
                if 1 <= this_one <= len(todos):
                    new_value = input("Enter the new value for the todo: ").capitalize() + "\n"
                    todos[this_one - 1] = new_value  # Replace the item in the list
                    with open(file_path, "w") as file:
                        file.writelines(todos)

                    print(f"Todo {this_one} updated to: {new_value}")
                else:
                    print(f"Invalid selection, please select between 1-{len(todos)}")
            else:
                print("Invalid input! Please enter a number.")
        else:
            print("No todos to edit.")

    if "complete" in user_response:
        if todos:
            print("Which todo would you like to mark as complete?")
            for index, todo in enumerate(todos, start=1):
                print(f"{index}. {todo.strip('\n')}")

            selection = input(f"Enter the number of the todo to complete (1-{len(todos)}): ")

            # Validate the input
            if selection.isdigit():
                selection = int(selection)
                if 1 <= selection <= len(todos):
                    removed_todo = todos.pop(selection - 1)  # Remove the selected todo
                    with open(file_path, 'w') as file:
                        file.writelines(todos)
                    print(f"Todo completed and removed: {removed_todo}")
                else:
                    print(f"Invalid selection, please select between 1-{len(todos)}")
            else:
                print("Invalid input! Please enter a number.")
        else:
            print("No todos to complete.")

    if "exit" in user_response:
        print("Bye!")
        break

