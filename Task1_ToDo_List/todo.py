import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Task added: {task}")


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, t in enumerate(tasks, 1):
        status = "Done" if t["done"] else "Not done"
        print(f"{i}. {t['task']} [{status}]")


def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Task marked as done: {tasks[index]['task']}")
    else:
        print("Invalid task number.")


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task deleted: {removed['task']}")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to mark done: ")) - 1
                mark_done(index)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "4":
            view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
