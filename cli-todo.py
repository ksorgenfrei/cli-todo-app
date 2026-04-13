print("\nTO DO LIST\n\nTo add a task, type 'add + task'\nTo delete, type 'delete + task'\nTo show the to do list, type 'show'\nTo exit, type 'exit'")

todo = []
going = True

while going:
    task = input()

    formattedTask = task.strip().lower()

    if formattedTask.startswith("add"):
        todo.append(task[4:])
    elif formattedTask.startswith("delete"):
        taskToDelete = task[7:]
        if taskToDelete not in todo:
            print("Task not found. Please check spelling.")
        else:
            todo.remove(taskToDelete)
    elif "show" in formattedTask:
        print("\nTO DO LIST:\n")
        for item in todo:
            print(f"{todo.index(item) + 1}. {item}")
    elif "exit" in formattedTask:
        going = False
    else:
        print("Invalid input. Please add or delete a task or show the to do list.")
