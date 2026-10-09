from sqlalchemy import Column, Integer, String
from task_db import Base


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    priority = Column(Integer, default=1, nullable=False)