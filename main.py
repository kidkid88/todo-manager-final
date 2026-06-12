from todo_manager.task import Task
from todo_manager.manager import TodoManager


manager = TodoManager()

task = Task(
    "파이썬 과제",
    "높음",
    "2025-06-20",
    ["학교", "과제"]
)

manager.add_task(task)

for t in manager.list_tasks():
    print(t)