from typing_extensions import Annotated
from sqlalchemy.orm import relationship, DeclarativeBase, mapped_column, Mapped
from sqlalchemy import func, ForeignKey, DateTime


class Base(DeclarativeBase):
    type_annotation_map = {}


intpk = Annotated[int, mapped_column(primary_key=True, index=True)]
user_fk = Annotated[int, mapped_column(ForeignKey("users.id"))]
dt = Annotated[DateTime, mapped_column(DateTime(timezone=True), server_default=func.now())]


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    name: Mapped[str]
    email: Mapped[str]

    results: Mapped[list["MathResult"]] = relationship("MathResult", back_populates="user")


class MathResult(Base):
    __tablename__ = "math_results"

    id: Mapped[intpk]
    user_id: Mapped[user_fk]
    question: Mapped[str]
    user_answer: Mapped[float]
    correct_answer: Mapped[float]
    feedback: Mapped[str]
    timestamp: Mapped[dt]

    user: Mapped["User"] = relationship("User", back_populates="results")
