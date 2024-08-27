import pytest
from api.user import crud
from api.user.models import Roles, User
from api.user.schemas import UserCreate, UserUpdate, SuperUserCreate
from sqlalchemy.orm import Session

from tests.utils.user import (
    create_random_email,
    create_random_string,
    create_random_user,
)


def test_create_user(session: Session) -> None:
    username = create_random_string()
    email = create_random_email()
    password = create_random_string()
    user_in = UserCreate(username=username, email=email, password=password)
    user = crud.create_user(session, user_in)

    assert user.username == username
    assert user.email == email
    assert user.role == Roles.USER
    assert hasattr(user, "password")


def test_create_user_existing_username(session: Session) -> None:
    user_1 = create_random_user(session)

    user_2 = UserCreate(
        username=user_1.username,
        email=create_random_email(),
        password=create_random_string(),
    )

    with pytest.raises(ValueError, match="Username already exists"):
        crud.create_user(session, user_2)


def test_create_user_existing_email(session: Session) -> None:
    user_1 = create_random_user(session)

    user_2 = UserCreate(
        username=create_random_string(),
        email=user_1.email,
        password=create_random_string(),
    )

    with pytest.raises(ValueError, match="Email already exists"):
        crud.create_user(session, user_2)


def test_create_superuser(session: Session) -> None:
    superuser = SuperUserCreate(
        username=create_random_string(),
        email=create_random_email(),
        password=create_random_string(),
        rolse=Roles.ADMIN,
    )
    db_superuser = crud.create_superuser(session, superuser)

    assert db_superuser.username == superuser.username
    assert db_superuser.email == superuser.email
    assert db_superuser.role == Roles.ADMIN
    assert hasattr(db_superuser, "password")


def test_read_user(session: Session) -> None:
    user = create_random_user(session)
    user_id = user.id
    db_user = crud.read_user(session, user_id)

    assert db_user == user


def test_read_user_not_found(session: Session) -> None:
    user_id = 99999999
    with pytest.raises(ValueError, match="User not found"):
        crud.read_user(session, user_id)


def test_read_all_users(session: Session) -> None:
    session.query(User).delete()
    session.commit()

    user_1 = create_random_user(session)
    user_2 = create_random_user(session)
    user_3 = create_random_user(session)

    db_users = crud.read_all_users(session)

    assert len(db_users) == 3
    assert user_1 in db_users
    assert user_2 in db_users
    assert user_3 in db_users

    assert all(isinstance(user, User) for user in db_users)


def test_read_all_users_empty(session: Session) -> None:
    session.query(User).delete()
    session.commit()

    with pytest.raises(ValueError, match="No users found"):
        crud.read_all_users(session)


def test_update_user(session: Session) -> None:
    user = create_random_user(session)
    user_data = UserUpdate(role=Roles.ADMIN)

    db_user = crud.update_user(session, user.id, user_data)

    assert db_user is not None
    assert db_user.role == Roles.ADMIN
    assert db_user.id == user.id


def test_update_user_not_found(session: Session) -> None:
    user_id = 99999999
    user_data = UserUpdate(role=Roles.ADMIN)

    with pytest.raises(ValueError, match="User not found"):
        crud.update_user(session, user_id, user_data)


def test_delete_user(session: Session) -> None:
    user = create_random_user(session)
    user_id = user.id

    db_user = crud.delete_user(session, user_id)

    assert db_user == user
    assert session.get(User, user_id) is None


def test_delete_user_not_found(session: Session) -> None:
    user_id = 99999999

    with pytest.raises(ValueError, match="User not found"):
        crud.delete_user(session, user_id)
