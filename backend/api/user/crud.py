from sqlalchemy.orm import Session

from api.core.security import get_password_hash

from .models import User, Roles
from .schemas import UserCreate, UserUpdate, SuperUserCreate


def create_user(db: Session, user: UserCreate):
    # check if username already exists
    db_username = db.query(User).filter(User.username == user.username).first()
    if db_username:
        raise ValueError("Username already exists")

    # check if email already exists
    db_email = db.query(User).filter(User.email == user.email).first()
    if db_email:
        raise ValueError("Email already exists")

    db_user = User(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_superuser(db: Session, user: SuperUserCreate):
    db_username = db.query(User).filter(User.username == user.username).first()
    if db_username:
        raise ValueError("Username already exists")

    db_email = db.query(User).filter(User.email == user.email).first()
    if db_email:
        raise ValueError("Email already exists")

    db_user = User(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
        role=Roles.ADMIN,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def read_user(db: Session, username: str):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user:
        raise ValueError("User not found")
    return db_user


def read_all_users(db: Session):
    db_users = db.query(User).all()
    if not db_users:
        raise ValueError("No users found")
    return db_users


def update_user(db: Session, user_id: int, user_data: UserUpdate):
    db_user = db.get(User, user_id)
    if not db_user:
        raise ValueError("User not found")

    for key, value in user_data.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.get(User, user_id)
    if not db_user:
        raise ValueError("User not found")

    db.delete(db_user)
    db.commit()
    return db_user
