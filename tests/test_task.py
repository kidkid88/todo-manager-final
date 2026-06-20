from todo_manager.core import Task
from todo_manager.subclass import RecurringTask


def test_task_creation():
    task = Task("과제", "높음", "2025-06-20")

    assert task.title == "과제"
    assert task.priority == "높음"


def test_task_completed_default():
    task = Task("과제", "높음", "2025-06-20")

    assert task.completed is False


def test_mark_completed():
    task = Task("과제", "높음", "2025-06-20")

    task.mark_completed()

    assert task.completed is True


def test_add_tag():
    task = Task("과제", "높음", "2025-06-20")

    task.add_tag("학교")

    assert "학교" in task.tags


def test_get_info():
    task = Task("과제", "높음", "2025-06-20")

    info = task.get_info()

    assert info["title"] == "과제"


def test_recurring_task_creation():
    task = RecurringTask(
        "운동",
        "중간",
        "2025-06-21",
        "매일"
    )

    assert task.repeat_cycle == "매일"


def test_recurring_task_info():
    task = RecurringTask(
        "운동",
        "중간",
        "2025-06-21",
        "매일"
    )

    info = task.get_info()

    assert info["repeat_cycle"] == "매일"


def test_empty_tag_list():
    task = Task(
        "과제",
        "높음",
        "2025-06-20"
    )

    assert task.tags == []
    