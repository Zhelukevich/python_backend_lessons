from app.repositories.task import TaskRepository
from app.schemas.task import TaskCreateSchema, TaskSchema, TaskUpdateSchema
from sqlalchemy.orm import Session


class TaskNotFound(Exception):
    """Задача не найдена"""


class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.task_repository = TaskRepository(db)

    def list_tasks(self) -> list[TaskSchema]:
        tasks = self.task_repository.get_all()
        return [TaskSchema.model_validate(task) for task in tasks]

    def create_task(self, task_create: TaskCreateSchema) -> TaskSchema:
        try:
            task = self.task_repository.create(title=task_create.title)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        return TaskSchema.model_validate(task)

    def update_task(self, task_id: str, task_update: TaskUpdateSchema) -> TaskSchema:
        task = self.task_repository.get_by_id(task_id=task_id)
        if task is None:
            raise TaskNotFound(f"Задача с id {task_id} не найдена")

        try:
            if task_update.title is not None:
                task.title = task_update.title
            if task_update.completed is not None:
                task.completed = task_update.completed
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        return TaskSchema.model_validate(task)

    def delete_task(self, task_id: str) -> None:
        task = self.task_repository.get_by_id(task_id=task_id)
        if task is None:
            raise TaskNotFound(f"Задача с id {task_id} не найдена")

        try:
            self.task_repository.delete(task)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
