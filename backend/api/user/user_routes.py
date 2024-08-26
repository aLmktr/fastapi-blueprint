from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from api.core.config import settings
from api.core.database import db_dependency
from api.core.security import CurrentUser, admin_user

from . import crud
from .schemas import UserCreate, UserPrivate, UserPublic, UserUpdate

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
    "/read-user/{user_id}",
    dependencies=[Depends(admin_user)],
    response_model=UserPrivate,
)
def read_user(db: db_dependency, user_id: int):
    try:
        db_user = crud.read_user(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return db_user


@router.get("/me", response_model=UserPublic)
def read_current_user(current_user: CurrentUser):
    return current_user


@router.get(
    "/read-users", dependencies=[Depends(admin_user)], response_model=List[UserPrivate]
)
def read_all_users(db: db_dependency):
    try:
        db_users = crud.read_all_users(db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return db_users


@router.patch(
    "/update/{user_id}", dependencies=[Depends(admin_user)], response_model=UserPrivate
)
def update_user(db: db_dependency, user_id: int, user_data: UserUpdate):
    try:
        db_user = crud.update_user(db, user_id, user_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return db_user


@router.delete(
    "/delete/{user_id}", dependencies=[Depends(admin_user)], response_model=UserPrivate
)
def delete_user(db: db_dependency, user_id: int):
    try:
        db_user = crud.delete_user(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return db_user
