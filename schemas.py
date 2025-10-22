from pydantic import BaseModel
from datetime import datetime


class MathResultBase(BaseModel):
    user_id: int
    question: str
    user_answer: float
    correct_answer: float


class MathResultCreate(MathResultBase):
    pass


class MathResultOut(MathResultBase):
    id: int
    feedback: str | None
    timestamp: datetime

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    name: str
    email: str


class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
