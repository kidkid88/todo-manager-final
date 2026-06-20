from .core import Task


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