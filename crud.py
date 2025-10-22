from sqlalchemy.orm import Session
import models
import schemas

def create_result(db: Session, data: schemas.MathResultCreate, feedback: str):
    res = models.MathResult(
        user_id = data.user_id,
        question = data.question,
        user_answer = data.user_answer,
        correct_answer = data.correct_answer,
        feedback = feedback,
    )
    db.add(res)
    db.commit()
    db.refresh(res)
    return res

def get_user_results(db: Session, user_id: int):
    q = db.query(models.MathResult).filter(models.MathResult.user_id == user_id).all()
    return q
