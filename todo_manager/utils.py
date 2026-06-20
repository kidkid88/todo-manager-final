def format_task(task):
    """
    Task 객체를 보기 좋은 문자열로 변환한다.

    Args:
        task (Task): 출력할 Task 객체

    Returns:
        str: 포맷된 문자열
    """
    return (
        f"[{task.priority}] "
        f"{task.title} "
        f"(마감일: {task.due_date})"
    )

