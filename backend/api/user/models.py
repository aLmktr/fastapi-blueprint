import enum
from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from api.core.database import Base


class Roles(enum.Enum):
    ADMIN = "admin"
    USER = "user"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(12), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(16), unique=True, index=True)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[Roles] = mapped_column(default=Roles.USER, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    created: Mapped[datetime] = mapped_column(server_default=func.now())
    updated: Mapped[datetime] = mapped_column(nullable=True, onupdate=func.now())
    last_login: Mapped[datetime] = mapped_column(nullable=True)
