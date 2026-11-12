from app.models.task import TaskORM
from sqlalchemy import select
from sqlalchemy.orm import Session


class TaskRepositories:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[TaskORM]:
        return list(self.db.scalars(select(TaskORM)).all())

    def get_by_id(self, task_id: str) -> TaskORM | None:
        return self.db.get(TaskORM, task_id)

    def create(self, title: str) -> TaskORM:
        new_task = TaskORM(title=title, completed=False)
        self.db.add(new_task)
        self.db.flush()
        return new_task

    def delete(self, task: TaskORM) -> None:
        self.db.delete(task)
