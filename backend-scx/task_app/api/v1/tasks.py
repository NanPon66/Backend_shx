from fastapi import APIRouter, Depends, HTTPException
from schemas.tasks import TaskIn, TaskResponse, UpdateTaskRequest
from services.tasks import TaskService

router = APIRouter(tags=["tasks"])


# Create
@router.post("/tasks", status_code=201, response_model=TaskResponse)
def create_task(raw_task: TaskIn, service: TaskService = Depends()):
    task = service.create_task(raw_task)
    if task["success"]:
        return TaskResponse(**task)
    else:
        raise HTTPException(status_code=400, detail=task["message"])


# Read collection (все объекты)
@router.get("/tasks", status_code=200)
def get_tasks(service: TaskService = Depends()):
    tasks = service.get_all_tasks()
    return tasks


# Read single (один объект)
@router.get("/tasks/{task_id}", status_code=200, response_model=TaskResponse)
def get_task_by_id(task_id: int, service: TaskService = Depends()):
    task = service.get_task_by_id(task_id)
    if task["success"]:
        return TaskResponse(**task)
    else:
        raise HTTPException(status_code=404, detail=task["message"])


# Update
@router.patch("/tasks/{task_id}", status_code=200, response_model=TaskResponse)
def update_task(task_id: int, upd_data: UpdateTaskRequest, service: TaskService = Depends()):
    task = service.edit_task(task_id, upd_data)
    if task["success"]:
        return TaskResponse(**task)
    else:
        raise HTTPException(status_code=404, detail=task["message"])


# Delete
@router.delete("/tasks/{task_id}", status_code=200)
def delete_task(task_id: int, service: TaskService = Depends()):
    delete_result = service.delete_task(task_id)
    if delete_result["success"]:
        return delete_result
    else:
        raise HTTPException(status_code=404, detail=delete_result["message"])