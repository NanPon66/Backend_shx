from fastapi import Depends
from sqlalchemy.orm import Session
from task_db import get_db
from models.tasks import TaskModel


class TaskRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_task_by_id(self, task_id: int):
        task = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if task:
            return {"id": task.id, "title": task.title, "priority": task.priority}
        return None

    def create_task(self, title: str, priority: int) -> dict:
        new_task = TaskModel(title=title, priority=priority)
        self.db.add(new_task)
        self.db.commit()
        self.db.refresh(new_task)
        return {"id": new_task.id, "title": new_task.title, "priority": new_task.priority}

    def get_all_tasks(self):
        tasks = self.db.query(TaskModel).all()
        return [{"id": t.id, "title": t.title, "priority": t.priority} for t in tasks]

    def edit_task(self, task_id: int, upd_data: dict):
        task = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if task:
            for key, value in upd_data.items():
                setattr(task, key, value)
            self.db.commit()
            self.db.refresh(task)

    def delete_task(self, task_id: int):
        task = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if task:
            self.db.delete(task)
            self.db.commit()