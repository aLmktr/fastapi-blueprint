from api.core.config import settings
from api.user import crud
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from tests.utils.user import (
    create_random_email,
    create_random_string,
    create_random_user,
)


def test_create_user(client: TestClient, session: Session):
    data = {
        "username": create_random_string(),
        "email": create_random_email(),
        "password": create_random_string(),
    }
    response = client.post(f"{settings.API_VER_STR}/user/create", json=data)

    assert 200 <= response.status_code < 300

    created_user_username = response.json()["username"]
    user = crud.read_user(session, created_user_username)

    assert user
    assert data["username"] == user.username
    assert data["email"] == user.email


def test_create_user_existing_username(client: TestClient, session: Session):
    user_1 = create_random_user(session)

    data = {
        "username": user_1.username,
        "email": create_random_email(),
        "password": create_random_string(),
    }

    response = client.post(f"{settings.API_VER_STR}/user/create", json=data)

    assert response.status_code == 400
    assert response.json() == {"detail": "Username already exists"}


def test_create_user_existing_email(client: TestClient, session: Session):
    user_1 = create_random_user(session)

    data = {
        "username": create_random_string(),
        "email": user_1.email,
        "password": create_random_string(),
    }

    response = client.post(f"{settings.API_VER_STR}/user/create", json=data)

    assert response.status_code == 400
    assert response.json() == {"detail": "Email already exists"}


def test_read_user_no_authentication(client: TestClient, session: Session):
    user = create_random_user(session)

    response = client.get(f"{settings.API_VER_STR}/user/read-user/{user.username}")

    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}
