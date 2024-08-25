from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
import bcrypt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session

from api.user.models import Roles, User

from .config import settings
from .database import db_dependency

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_VER_STR}/auth/login/")
oauth2_dependency = Annotated[str, Depends(oauth2_scheme)]


def create_access_token(
    subject: str,
    expires_delta: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_EXPI_MIN),
):
    expire = datetime.now(timezone.utc) + expires_delta
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def get_password_hash(password: str):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str):
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


def authenticate_user(db: Session, username: str, password: str):
    db_user = db.query(User).filter(User.username == username).first()

    if not db_user:
        raise ValueError("User not found")

    if not verify_password(password, db_user.password):
        raise ValueError("Incorrect username or password")

    if not db_user.is_active:
        raise ValueError("User is not active")

    return db_user


def current_user(db: db_dependency, token: oauth2_dependency):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = payload.get("sub")
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = db.get(User, int(token_data))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


CurrentUser = Annotated[User, Depends(current_user)]


def admin_user(current_user: CurrentUser):
    if not current_user.role == Roles.ADMIN:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return current_user
