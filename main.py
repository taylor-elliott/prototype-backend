from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

import joblib

import models
import schemas
import crud
import database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)


model = joblib.load("models/feedback_model.joblib")


@app.post("/submit", response_model=schemas.MathResultOut)
def submit_result(data: schemas.MathResultCreate, db: Session = Depends(database.get_db)):
    x = [[data.user_answer, data.correct_answer]]
    feedback = model.predict(x)[0]
    res = crud.create_result(db, data, feedback)
    return res

@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    res = crud.check_unique_email(db, user.email)
    if res:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

@app.get("/users", response_model=list[schemas.UserOut])
def get_all_users(db: Session = Depends(database.get_db)):
    res = crud.get_all_users(db)
    return res

@app.get("/users/{user_id}", response_model=list[schemas.MathResultOut])
def get_user_results(user_id: int, db: Session = Depends(database.get_db)):
    res = crud.get_user_results(db, user_id)
    return res


@app.get("/questions", response_model=list[schemas.QuestionOut])
def get_all_questions(db: Session = Depends(database.get_db)):
    res = crud.get_all_questions(db)
    return res

