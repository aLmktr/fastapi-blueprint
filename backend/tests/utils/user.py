import random
import string

from sqlalchemy.orm import Session


from api.user import crud
from api.user.models import User
from api.user.schemas import UserCreate


def create_random_string(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))


def create_random_email() -> str:
    return f"{create_random_string()}@{create_random_string()}.com"


def create_random_user(db: Session) -> User:
    user_in = UserCreate(
        username=create_random_string(),
        email=create_random_email(),
        password=create_random_string(),
    )
    user = crud.create_user(db, user_in)

    return user
