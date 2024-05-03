# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to mark a task as completed
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

# Function to remove a task
def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task removed successfully!")
    else:
        print("Invalid task index.")

# Function to display all tasks
def display_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i+1}. {task['task']} - {status}")
    else:
        print("No tasks available.")

# Main function
def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Remove Task")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            complete_task(task_index)
        elif choice == "3":
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            remove_task(task_index)
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
