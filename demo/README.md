# Todo List App

A minimal command-line todo list that persists tasks to `todos.json`.

## Requirements

Python 3.6+. No external dependencies.

## Usage

Run all commands from inside the `demo/` directory:

```bash
# Add a todo
python todo.py add Buy groceries

# List all todos
python todo.py list

# Mark a todo as complete (use the id shown in list)
python todo.py complete 1

# Delete a todo
python todo.py delete 1
```

## Example session

```
$ python todo.py add Buy groceries
Added #1: Buy groceries

$ python todo.py add Write report
Added #2: Write report

$ python todo.py list
[ ] #1: Buy groceries
[ ] #2: Write report

$ python todo.py complete 1
Completed #1: Buy groceries

$ python todo.py list
[x] #1: Buy groceries
[ ] #2: Write report

$ python todo.py delete 1
Deleted #1.

$ python todo.py list
[ ] #2: Write report
```

## Data storage

Todos are saved in `todos.json` next to `todo.py`. Delete that file to reset all todos.
