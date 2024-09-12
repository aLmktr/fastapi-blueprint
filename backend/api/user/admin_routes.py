from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from api.core.config import settings
from api.core.database import db_dependency
from api.core.security import admin_user

from . import crud
from .schemas import UserPrivate, UserUpdate

router = APIRouter(
    prefix=f"{settings.API_VER_STR}/admin",
    tags=["admin"],
)


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
