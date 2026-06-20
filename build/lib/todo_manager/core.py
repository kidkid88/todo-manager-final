class Task:
    """할 일을 표현하는 부모 클래스."""

    def __init__(
        self,
        title,
        priority,
        due_date,
        tags=None
    ):
        """
        Task 객체 생성.

        Args:
            title (str): 할 일 제목
            priority (str): 우선순위
            due_date (str): 마감일
            tags (list): 태그 목록
        """
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.tags = tags or []
        self.completed = False

    def mark_completed(self):
        """할 일을 완료 상태로 변경한다."""
        self.completed = True

    def add_tag(self, tag):
        """새로운 태그를 추가한다."""
        self.tags.append(tag)

    def get_info(self):
        """할 일 정보를 딕셔너리 형태로 반환한다."""
        return {
            "title": self.title,
            "priority": self.priority,
            "due_date": self.due_date,
            "tags": self.tags,
            "completed": self.completed
        }
