import json
import os
import sys

DATA_FILE = os.path.join(os.path.dirname(__file__), "todos.json")


def _load():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def _save(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def add(title):
    todos = _load()
    todo = {"id": (todos[-1]["id"] + 1) if todos else 1, "title": title, "done": False}
    todos.append(todo)
    _save(todos)
    print(f"Added #{todo['id']}: {title}")


def list_todos():
    todos = _load()
    if not todos:
        print("No todos.")
        return
    for t in todos:
        status = "x" if t["done"] else " "
        print(f"[{status}] #{t['id']}: {t['title']}")


def complete(todo_id):
    todos = _load()
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = True
            _save(todos)
            print(f"Completed #{todo_id}: {t['title']}")
            return
    print(f"No todo with id {todo_id}.")


def delete(todo_id):
    todos = _load()
    remaining = [t for t in todos if t["id"] != todo_id]
    if len(remaining) == len(todos):
        print(f"No todo with id {todo_id}.")
        return
    _save(remaining)
    print(f"Deleted #{todo_id}.")


def main():
    commands = {"add": add, "list": list_todos, "complete": complete, "delete": delete}

    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print("Usage: python todo.py <add|list|complete|delete> [args]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "list":
        list_todos()
    elif cmd == "add":
        if len(sys.argv) < 3:
            print("Usage: python todo.py add <title>")
            sys.exit(1)
        add(" ".join(sys.argv[2:]))
    elif cmd in ("complete", "delete"):
        if len(sys.argv) < 3:
            print(f"Usage: python todo.py {cmd} <id>")
            sys.exit(1)
        commands[cmd](int(sys.argv[2]))


if __name__ == "__main__":
    main()
