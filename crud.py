from sqlalchemy.orm import Session
from sqlalchemy import select
from passlib.context import CryptContext
import models
import schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=get_password_hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_result(db: Session, data: schemas.MathResultCreate, feedback: str):
    r = models.MathResult(
        user_id=data.user_id,
        question=data.question,
        user_answer=data.user_answer,
        correct_answer=data.correct_answer,
        feedback=feedback,
    )
    db.add(r)
    db.commit()
    db.refresh(r)
    return r


def check_unique_email(db: Session, email: str):
    q = select(models.User).where(models.User.email == email)
    r = db.scalars(q).first()
    return r

def get_all_questions(db: Session):
    q = select(models.Question)
    r = db.scalars(q).all()
    return r

def get_all_users(db: Session):
    q = select(models.User)
    r = db.scalars(q).all()
    return r

def get_user_results(db: Session, user_id: int):
    q = select(models.MathResult).where(models.MathResult.user_id == user_id)
    r = db.scalars(q).all()
    return r
