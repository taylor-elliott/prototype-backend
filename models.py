from typing_extensions import Annotated
from sqlalchemy.orm import relationship, DeclarativeBase, mapped_column, Mapped
from sqlalchemy import func, ForeignKey, DateTime


class Base(DeclarativeBase):
    type_annotation_map = {}


intpk = Annotated[int, mapped_column(primary_key=True, index=True)]
user_fk = Annotated[int, mapped_column(ForeignKey("users.id"))]
module_fk = Annotated[int, mapped_column(ForeignKey("modules.id"))]
q_fk = Annotated[int, mapped_column(ForeignKey("questions.id"))]
dt = Annotated[DateTime, mapped_column(DateTime(timezone=True), server_default=func.now())]


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    name: Mapped[str]
    email: Mapped[str]
    hashed_password: Mapped[str]

    results: Mapped[list["MathResult"]] = relationship("MathResult", back_populates="user")
    questions: Mapped[list["Question"]] = relationship("Question", back_populates="user")

    def __repr__(self) -> str:
        return (
            f"User(id={self.id!r}, name={self.name!r}, email={self.email!r}, "
            f"results_count={len(self.results) if self.results is not None else 0})"
        )


class MathResult(Base):
    __tablename__ = "math_results"

    id: Mapped[intpk]
    user_id: Mapped[user_fk]
    question_id: Mapped[q_fk]
    user_answer: Mapped[float]
    feedback: Mapped[str]
    timestamp: Mapped[dt]

    user: Mapped["User"] = relationship("User", back_populates="results")
    question: Mapped["Question"] = relationship("Question")

    def __repr__(self) -> str:
        return (
            f"MathResult(id={self.id!r}, user_id={self.user_id!r}, question_id={self.question_id!r}, "
            f"user_answer={self.user_answer!r}, feedback={self.feedback!r}, timestamp={self.timestamp!r})"
        )

class Modules(Base):
    __tablename__ = "modules"

    id: Mapped[intpk]
    name: Mapped[str]

    questions: Mapped[list["Question"]] = relationship("Question", back_populates="module")

    def __repr__(self) -> str:
        return f"Modules(id={self.id!r}, name={self.name!r}, questions_count={len(self.questions) if self.questions else 0})"


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[intpk]
    user_id: Mapped[user_fk]
    module_id: Mapped[module_fk]
    type: Mapped[str]
    topic: Mapped[str]
    question: Mapped[str]
    correct_answer: Mapped[float]
    diff: Mapped[int]

    user: Mapped["User"] = relationship("User", back_populates="questions")
    module: Mapped["Modules"] = relationship("Modules", back_populates="questions")

    def __repr__(self) -> str:
        return (
            f"Question(id={self.id!r}, user_id={self.user_id!r}, module_id={self.module_id!r}, "
            f"type={self.type!r}, question={self.question!r}, correct_answer={self.correct_answer!r}, diff={self.diff!r})"
        )

