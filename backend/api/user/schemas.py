from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from .models import Roles


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class SuperUserCreate(UserCreate):
    role: Roles = Roles.ADMIN


class UserPublic(BaseModel):
    username: str
    email: str
    role: str
    created: datetime
    last_login: datetime | None = None


class UserPrivate(UserPublic):
    id: int
    updated: datetime | None = None


class UserUpdate(BaseModel):
    role: Optional[Roles] = Roles.USER
