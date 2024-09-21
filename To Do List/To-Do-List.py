import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return

    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

    try:
        choice = int(input("Enter task number to remove: ")) - 1
        if 0 <= choice < len(tasks):
            del tasks[choice]
            print("Task removed!")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input.")

def display_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("Tasks")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()