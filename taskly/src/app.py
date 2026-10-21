import sys

tasks = []

def add_task(title):
    tasks.append({"title": title, "done": False})
    return len(tasks)

def list_tasks():
    for i, t in enumerate(tasks, 1):
        mark = "x" if t["done"] else " "
        print(f"{i}. [{mark}] {t['title']}")

def main(argv):
    if len(argv) < 2:
        print("usage: app.py add|list")
        return 1
    if argv[1] == "add":
        add_task(" ".join(argv[2:]))
    elif argv[1] == "list":
        list_tasks()
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
