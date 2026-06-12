class RecurringTask(Task):
    def __init__(
        self,
        title,
        priority,
        due_date,
        repeat_cycle,
        tags=None
    ):
        super().__init__(
            title,
            priority,
            due_date,
            tags
        )

        self.repeat_cycle = repeat_cycle

    def __str__(self):
        return (
            f"RecurringTask("
            f"title={self.title}, "
            f"repeat_cycle={self.repeat_cycle})"
        )