from fastapi import Depends
from sqlalchemy.orm import Session
from task_db import get_db
from models.users import UserModel


class UserRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_user_by_username(self, username: str):
        user = self.db.query(UserModel).filter(UserModel.username == username).first()
        if user:
            return {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "password": user.password,
            }
        return None

    def create_user(self, username: str, email: str, password: str):
        new_user = UserModel(username=username, email=email, password=password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
            "password": new_user.password,
        }

    def get_all_users(self):
        users = self.db.query(UserModel).all()
        return [
            {
                "id": u.id,
                "username": u.username,
                "email": u.email,
                "password": u.password,
            }
            for u in users
        ]

    def edit_user(self, username: str, upd_data: dict):
        user = self.db.query(UserModel).filter(UserModel.username == username).first()
        if user:
            for key, value in upd_data.items():
                setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)

    def delete_user(self, username: str):
        user = self.db.query(UserModel).filter(UserModel.username == username).first()
        if user:
            self.db.delete(user)
            self.db.commit()