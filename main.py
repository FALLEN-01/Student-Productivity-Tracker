print("----------------------------------")
print("  Student Productivity Tracker")
print("----------------------------------")

while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task description: ")
        priority = input("Enter the priority (High/Medium/Low): ")
        status="pending"
        with open("tasks.txt", "a") as file:
            file.write(f"{task} | priority: {priority} | status: {status}\n")
        print("Task added successfully!")
    elif choice == '2':
        print("\nYour Tasks:")
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task.strip()}")
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")