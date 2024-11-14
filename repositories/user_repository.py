from sqlalchemy.orm import Session
from models.user import User
from models.schemas import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email, phone=user.phone, company_id=user.company_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user