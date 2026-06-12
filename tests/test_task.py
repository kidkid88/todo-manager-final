from todo_manager.task import Task


def test_task_creation():
    task = Task(
        "테스트",
        "높음",
        "2025-01-01"
    )

    assert task.title == "테스트"