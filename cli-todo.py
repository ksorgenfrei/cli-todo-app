import json
print("\nTO DO LIST\n\nTo add a task, type 'add + task'\nTo delete, type 'delete + task'\n To complete a task, type 'complete + task'\nTo show the to do list, type 'show'\nTo exit, type 'exit'")

def load_tasks():
    try:
        with open("tasks.json") as f:
            tasks = json.load(f)
            return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks: list):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=1)

tasks = load_tasks()

going = True

while going:
    task = input()

    formattedTask = task.strip().lower()

    if formattedTask.startswith("add"):
        tasks.append({"task": task[4:].strip(), "done": False})
        save_tasks(tasks)
    
    elif formattedTask.startswith("complete"):
        for item in tasks:
            if item["task"] == task[9:].strip():
                item["done"] = True
        save_tasks(tasks)

    elif formattedTask.startswith("delete"):
        taskToDelete = task[7:].strip()
        for item in tasks:
            if item["task"] == taskToDelete:
                print(f'Task "{item["task"]}" deleted.')
                tasks.remove(item)
                break
        save_tasks(tasks)


    elif formattedTask.startswith("show"):
        print("\nTO DO LIST:\n")
        for index, item in enumerate(tasks, start=1):
            if item["done"] == False:
                print(f'{index}. [ ] {item["task"]}')
            else:
                print(f'{index}. [x] {item["task"]}')
   
    elif formattedTask.startswith("exit"):
        going = False

    else:
        print('Invalid input. Please add or delete a task or show the to do list.')
