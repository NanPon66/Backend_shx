from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Замените логин, пароль, хост, порт и имя БД на ваши актуальные данные PostgreSQL:
DATABASE_URL = "postgresql+psycopg2://postgres:628Aa12@localhost:5432/task_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()