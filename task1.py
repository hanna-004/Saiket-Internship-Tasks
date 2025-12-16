class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔ Completed" if self.completed else "✗ Not Completed"
        return f"{self.description} [{status}]"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks added yet!")
            return
        
        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def mark_task_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number!")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f"Task '{removed.description}' removed successfully!")
        else:
            print("Invalid task number!")


def main():
    todo = ToDoList()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo.add_task(description)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            todo.view_tasks()
            task_num = int(input("Enter task number to mark completed: "))
            todo.mark_task_completed(task_num)

        elif choice == "4":
            todo.view_tasks()
            task_num = int(input("Enter task number to remove: "))
            todo.remove_task(task_num)

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()
