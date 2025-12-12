import json
import os

STORAGE_FILE = "storage.json"


def load_tasks():
    """Load tasks from JSON file"""
    if not os.path.exists(STORAGE_FILE):
        return []

    with open(STORAGE_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(STORAGE_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"✔ Task added: {task}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return

    print("\nYour To-Do List:")
    for idx, item in enumerate(tasks, start=1):
        status = "✓" if item["completed"] else "✗"
        print(f"{idx}. {item['task']}  [{status}]")
    print("")


def mark_complete(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f"✔ Task completed: {tasks[index]['task']}")
    else:
        print("Invalid task number!")


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑 Deleted: {removed['task']}")
    else:
        print("Invalid task number!")


def menu():
    print("\n=== TO-DO LIST APP ===")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        index = int(input("Enter task number: ")) - 1
        mark_complete(index)
    elif choice == "4":
        index = int(input("Enter task number: ")) - 1
        delete_task(index)
    elif choice == "5":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    while True:
        menu()

