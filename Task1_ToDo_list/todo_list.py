# CodSoft Python Programming Internship
# Task 1 - To-Do List Application

tasks = []


def add_task():
    task = input("Enter a new task: ")

    if task.strip() == "":
        print("Task cannot be empty!")
        return

    tasks.append({
        "task": task,
        "completed": False
    })

    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== YOUR TASKS ==========")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['task']} [{status}]")

    print("================================")


def update_task():
    if not tasks:
        print("\nNo tasks available to update.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to update: "))

        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the updated task: ")

            if new_task.strip() == "":
                print("Task cannot be empty!")
                return

            tasks[task_number - 1]["task"] = new_task

            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def complete_task():
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_number = int(
            input("Enter task number to mark as completed: ")
        )

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    if not tasks:
        print("\nNo tasks available to delete.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(
                f"Task '{deleted_task['task']}' deleted successfully!"
            )
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n====================================")
        print("       TO-DO LIST APPLICATION")
        print("====================================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            complete_task()

        elif choice == "5":
            delete_task()

        elif choice == "6":
            print("Thank you for using the To-Do List Application!")
            break

        else:
            print("Invalid choice. Please try again.")


main()