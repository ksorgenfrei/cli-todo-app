import json
print("\nTO DO LIST\n\nTo add a task, type 'add + task'\nTo delete, type 'delete + task'\nTo complete a task, type 'complete + task'\nTo show the to do list, type 'show'\nTo exit, type 'exit'")

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

    formatted_task = task.strip().lower()

    if formatted_task.startswith("add"):
        task = task[4:].strip()
        if any(item.get("task") == task for item in tasks):
            print(f'Task "{task}" is already on the to do list.')
        else:
            tasks.append({"task": task, "done": False})
            print(f'Task "{task}" added.')
        save_tasks(tasks)

    
    elif formatted_task.startswith("complete"):
        task = task[9:].strip()
        for item in tasks:
            if item["task"] == task:
                print(f'Task "{task}" completed.')
                item["done"] = True
        save_tasks(tasks)

    elif formatted_task.startswith("delete"):
        task_to_delete = task[7:].strip()
        for item in tasks:
            if item["task"] == task_to_delete:
                print(f'Task "{item["task"]}" deleted.')
                tasks.remove(item)
                break
        save_tasks(tasks)


    elif formatted_task.startswith("show"):
        print("\nTO DO LIST:\n")
        for index, item in enumerate(tasks, start=1):
            if item["done"] == False:
                print(f'{index}. [ ] {item["task"]}')
            else:
                print(f'{index}. [x] {item["task"]}')
   
    elif formatted_task.startswith("exit"):
        going = False

    else:
        print('Invalid input. Please add or delete a task or show the to do list.')
