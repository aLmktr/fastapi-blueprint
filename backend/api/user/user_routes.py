from fastapi import APIRouter, HTTPException, status

from api.core.config import settings
from api.core.database import db_dependency
from api.core.security import CurrentUser

from . import crud
from .schemas import UserCreate, UserPrivate, UserPublic

router = APIRouter(
    prefix=f"{settings.API_VER_STR}/user",
    tags=["user"],
)


@router.post("/create", response_model=UserPublic)
def create_user(db: db_dependency, user: UserCreate):
    try:
        db_user = crud.create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return db_user


@router.get(
    "/read-user/{username}",
    response_model=UserPrivate,
)
def read_user(db: db_dependency, username: str, current_user: CurrentUser):
    try:
        db_user = crud.read_user(db, username)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return db_user


@router.get("/me", response_model=UserPublic)
def read_current_user(current_user: CurrentUser):
    return current_user
