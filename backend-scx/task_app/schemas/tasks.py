from typing import Optional
from pydantic import BaseModel, Field


class TaskIn(BaseModel):
    title: str
    priority: int = Field(default=1, ge=1, le=5)


# Псевдоним для единообразия с CreateUserRequest
CreateTaskRequest = TaskIn


class TaskResponse(BaseModel):
    id: int
    title: str
    priority: int


class UpdateTaskRequest(BaseModel):
    title: Optional[str] = None
    priority: Optional[int] = Field(default=None, ge=1, le=5)