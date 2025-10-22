from database import SessionLocal, engine, Base
from models import User, MathResult

Base.metadata.create_all(bind=engine)

db = SessionLocal()

users = [
    User(name="Taylor", email="taylor@uoguelph.com"),
    User(name="Elliott", email="elliott@uoguelph.com"),
    User(name="Douglas", email="douglas@uoguelph.com"),
]

db.add_all(users)
db.commit()

users_in_db = db.query(User).all()
user_map = {u.name: u.id for u in users_in_db}

results = [
    MathResult(user_id=user_map['Taylor'], question='5 + 7', user_answer=12, correct_answer=12, feedback='Correct!'),
    MathResult(user_id=user_map['Taylor'], question='8 × 7', user_answer=55, correct_answer=56, feedback='Almost correct, check your multiplication'),
    MathResult(user_id=user_map['Elliott'], question='10 - 3', user_answer=7, correct_answer=7, feedback='Correct!'),
    MathResult(user_id=user_map['Elliott'], question='15 ÷ 3', user_answer=6, correct_answer=5, feedback='Incorrect, check division'),
    MathResult(user_id=user_map['Douglas'], question='9 × 9', user_answer=81, correct_answer=81, feedback='Correct!'),
    MathResult(user_id=user_map['Douglas'], question='12 + 8', user_answer=19, correct_answer=20, feedback='Almost correct, check addition'),
]

db.add_all(results)
db.commit()
db.close()

print("DATABASE SEEDED")
