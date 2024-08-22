from typing import Optional

from pydantic import BaseModel

from .models import Roles


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserPblic(BaseModel):
    username: str
    email: str
    role: str
    created: str
    last_login: str


class UserPrivate(UserPblic):
    id: int
    password: str
    updated: str


class UserUpdate(BaseModel):
    role: Optional[Roles] = Roles.USER
