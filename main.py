from todo_manager.core import Task
from todo_manager.subclass import RecurringTask
from todo_manager.utils import format_task


task1 = Task(
    "과제 제출",
    "높음",
    "2025-06-20"
)

task2 = RecurringTask(
    "운동",
    "중간",
    "2025-06-21",
    "매일"
)

print(format_task(task1))
print(task2.get_info())