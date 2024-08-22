from fastapi import APIRouter, HTTPException, status

from api.core.database import db_dependency

from . import services
from .schemas import UserCreate, UserUpdate

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("/create")
def create_user(db: db_dependency, user: UserCreate):
    try:
        db_user = services.create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return db_user


@router.get("/read/{user_id}")
def read_user(db: db_dependency, user_id: int):
    try:
        db_user = services.read_user(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return db_user


@router.get("/read-all")
def read_all_users(db: db_dependency):
    try:
        db_users = services.read_all_users(db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return db_users


@router.patch("/update/{user_id}")
def update_user(db: db_dependency, user_id: int, user_data: UserUpdate):
    try:
        db_user = services.update_user(db, user_id, user_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return db_user


@router.delete("/delete/{user_id}")
def delete_user(db: db_dependency, user_id: int):
    try:
        db_user = services.delete_user(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return db_user
