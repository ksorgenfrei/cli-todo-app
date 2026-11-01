# cli-todo-app - A to do list app in python

A small command-line to do list I made in Python to practice working with user input, lists, dictionaries, functions, and JSON files. No AI was used for this project, as I used it to practice writing code "by hand".

The app lets you add, complete, delete, and view tasks while preventing duplicated entries. It saves everything to `tasks.json`, so the list is still there the next time it is run.

## Commands

- `add <task>` — adds a new task
- `complete <task>` — marks a task as complete
- `delete <task>` — removes a task
- `show` — displays the to-do list
- `exit` — closes the program

The program also checks for duplicates and prevents adding a task that already exists.

## Running it

Run the Python file from the terminal:

`python3 todo.py`

The program will create `tasks.json` automatically the first time it saves a task.

## What I practiced

This was mainly a small practice project to get more comfortable with Python basics I was exposed to during my studies, including:

- working with lists and dicts
- reading and writing JSON
- functions
- loops and conditionals
- string handling
- checking existing data before adding new entries
- data persistence