class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task] = "Incomplete"
        print(f"Task '{task}' added.")

    def mark_task_as_completed(self, task):
        if task in self.tasks:
            self.tasks[task] = "Complete"
            print(f"Task '{task}' marked as complete.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("\nTo-Do List:")
            for task, status in self.tasks.items():
                print(f"{task}: {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Application =====")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to mark as completed: ")
            todo_list.mark_task_as_completed(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
