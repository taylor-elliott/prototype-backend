from database import SessionLocal, engine
from models import Base, User, MathResult, Modules, Question

Base.metadata.create_all(bind=engine)

db = SessionLocal()

modules = [
    Modules(name="Addition"),
    Modules(name="Subtraction"),
    Modules(name="Multiplication"),
    Modules(name="Division"),
]
db.add_all(modules)
db.commit()

modules_in_db = db.query(Modules).all()
module_map = {m.name: m.id for m in modules_in_db}

users = [
    User(name="Taylor", email="taylor@uoguelph.com", hashed_password="$2b$12$ACVe.7AlQbxNC4hhiZbIIOybT/9d8zbJ2XSeLv37p3hk.nAHG7Gsq"),
    User(name="Elliott", email="elliott@uoguelph.com", hashed_password="$2b$12$ACVe.7AlQbxNC4hhiZbIIOybT/9d8zbJ2XSeLv37p3hk.nAHG7Gsq"),
    User(name="Douglas", email="douglas@uoguelph.com", hashed_password="$2b$12$ACVe.7AlQbxNC4hhiZbIIOybT/9d8zbJ2XSeLv37p3hk.nAHG7Gsq"),
]
db.add_all(users)
db.commit()

users_in_db = db.query(User).all()
user_map = {u.name: u.id for u in users_in_db}

questions = [
    Question(
        user_id=user_map["Taylor"],
        module_id=module_map["Addition"],
        question="5 + 7",
        type="multiple-choice",
        topic="math",
        correct_answer=12,
        diff=1
    ),
    Question(
        user_id=user_map["Taylor"],
        module_id=module_map["Multiplication"],
        question="8 × 7",
        type="multiple-choice",
        topic="math",
        correct_answer=56,
        diff=2
    ),
    Question(
        user_id=user_map["Elliott"],
        module_id=module_map["Subtraction"],
        question="10 - 3",
        type="multiple-choice",
        topic="math",
        correct_answer=7,
        diff=1
    ),
    Question(
        user_id=user_map["Elliott"],
        module_id=module_map["Division"],
        question="15 ÷ 3",
        type="multiple-choice",
        topic="math",
        correct_answer=5,
        diff=1
    ),
    Question(
        user_id=user_map["Douglas"],
        module_id=module_map["Multiplication"],
        question="9 × 9",
        type="multiple-choice",
        topic="math",
        correct_answer=81,
        diff=3
    ),
    Question(
        user_id=user_map["Douglas"],
        module_id=module_map["Addition"],
        question="12 + 8",
        type="multiple-choice",
        topic="math",
        correct_answer=20,
        diff=2
    ),
]
db.add_all(questions)
db.commit()

questions_in_db = db.query(Question).all()
question_map = {q.question: q.id for q in questions_in_db}

# (normalized)
results = [
    MathResult(
        user_id=user_map["Taylor"],
        question_id=question_map["5 + 7"],
        user_answer=12,
        feedback="Correct!"
    ),
    MathResult(
        user_id=user_map["Taylor"],
        question_id=question_map["8 × 7"],
        user_answer=55,
        feedback="Almost correct, check your multiplication."
    ),
    MathResult(
        user_id=user_map["Elliott"],
        question_id=question_map["10 - 3"],
        user_answer=7,
        feedback="Correct!"
    ),
    MathResult(
        user_id=user_map["Elliott"],
        question_id=question_map["15 ÷ 3"],
        user_answer=6,
        feedback="Incorrect, check division."
    ),
    MathResult(
        user_id=user_map["Douglas"],
        question_id=question_map["9 × 9"],
        user_answer=81,
        feedback="Correct!"
    ),
    MathResult(
        user_id=user_map["Douglas"],
        question_id=question_map["12 + 8"],
        user_answer=19,
        feedback="Almost correct, check addition."
    ),
]
db.add_all(results)
db.commit()

db.close()
print("✅ DATABASE SEEDED SUCCESSFULLY")

