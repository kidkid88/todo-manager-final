class Task:
    def __init__(self, title, priority, due_date, tags=None):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.tags = tags or []

    def __str__(self):
        return (
            f"Task(title={self.title}, "
            f"priority={self.priority}, "
            f"due_date={self.due_date})"
        )