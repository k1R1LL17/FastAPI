import pytest 
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app  
from app.config.config import get_users_collection  

@pytest.fixture
def mock_user_collection():
    return MagicMock()

@pytest.fixture
def client(mock_user_collection):
    app.dependency_overrides[get_users_collection] = lambda: mock_user_collection
    return TestClient(app)

@pytest.fixture
def access_token_admin(client):
    login_data = {"login": "admin", "password": "Admin888@"}
    response = client.post("api/v1/auth/login", json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.cookies
    return response.cookies["access_token"]

@pytest.fixture
def access_token_user(client):
    login_data = {"login": "user", "password": "User123@"}
    response = client.post("api/v1/auth/login", json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.cookies
    return response.cookies["access_token"]
