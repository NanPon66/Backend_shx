from fastapi import Depends
from repositories.tasks import TaskRepository
from schemas.tasks import TaskIn, UpdateTaskRequest


class TaskService:
    def __init__(self, repository: TaskRepository = Depends()):
        self.repository = repository

    def create_task(self, raw_task: TaskIn):
        task = self.repository.create_task(raw_task.title, raw_task.priority)
        return {"success": True, **task}

    def get_all_tasks(self):
        tasks = self.repository.get_all_tasks()
        return tasks

    def get_task_by_id(self, task_id: int):
        task = self.repository.get_task_by_id(task_id)
        if task:
            return {"success": True, **task}
        else:
            return {"success": False, "message": "Task not found."}

    def edit_task(self, task_id: int, upd_data: UpdateTaskRequest):
        if not self.repository.get_task_by_id(task_id):
            return {"success": False, "message": "Task not found."}
        else:
            upd_data_dict = upd_data.model_dump()
            clear_dict = {k: v for k, v in upd_data_dict.items() if v is not None}

            self.repository.edit_task(task_id, clear_dict)
            updated_task = self.repository.get_task_by_id(task_id)
            return {"success": True, **updated_task}

    def delete_task(self, task_id: int):
        if not self.repository.get_task_by_id(task_id):
            return {"success": False, "message": "Task not found."}
        else:
            self.repository.delete_task(task_id)
            return {"success": True, "message": "Task was deleted."}