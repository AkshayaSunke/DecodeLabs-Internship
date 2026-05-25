tasks = []
task_id = 1
while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Exit")
    choice = input("Enter your choice: ")
# ADD TASK
    if choice == "1":
         task_name = input("Enter task: ")

         task = {
            "id": task_id,
            "name": task_name
        }

         tasks.append(task)

         print("Task Added Successfully!")
         task_id += 1
# VIEW TASKS
    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i in range(len(tasks)):
                print(f"ID: {tasks[i]['id']} | Task: {tasks[i]['name']}")
# SEARCH TASK
    elif choice == "3":

        search = input("Enter task name to search: ")

        found = False

        for task in tasks:

            if search.lower() in task["name"].lower():

                print(f"Found -> ID: {task['id']} | Task: {task['name']}")

                found = True
        if not found:
            print("Task not found.")
 # EXIT
    elif choice == "4":

        print("Program Closed.")
        break
# INVALID CHOICE
    else:
        print("Invalid Choice!")