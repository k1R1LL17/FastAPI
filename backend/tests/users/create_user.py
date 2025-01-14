from unittest.mock import MagicMock  
from tests.base import client, access_token_admin, access_token_user, mock_user_collection

def test_create_user_with_admin_role(client, access_token_admin, mock_user_collection):
    user_data = {
        "login": "newuser",
        "password": "newpassword@99A",
        "name": "New",
        "last_name": "User",
        "age": 30,
        "role_id": "6781177cf2e31cc2c6b2b7fb" 
    }

    mock_user_collection.insert_one.return_value = MagicMock(inserted_id="12345")

    response = client.post(
        "/api/v1/users/create/user",
        json=user_data,
        cookies={"access_token": access_token_admin} 
    )

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["login"] == "newuser"
    assert response_data["name"] == "New"
    assert response_data["last_name"] == "User"
    assert response_data["age"] == 30
    assert response_data["role_id"] == "6781177cf2e31cc2c6b2b7fb" 

def test_create_user_with_user_role(client, access_token_user, mock_user_collection):
    user_data = {
        "login": "newuser",
        "password": "newpassword@99A",
        "name": "New",
        "last_name": "User",
        "age": 30,
        "role_id": "6781177cf2e31cc2c6b2b7fb",
        "email": "user@example.com"
    }

    mock_user_collection.insert_one.return_value = MagicMock(inserted_id="12345")

    response = client.post(
        "/api/v1/users/create/user",
        json=user_data,  
        cookies={"access_token": access_token_user} 
    )

    assert response.status_code == 403 
    assert response.json() == {"detail": "You don't have permission"}

def test_create_user_unathorized(client, mock_user_collection):
    user_data = {
        "login": "newuser",
        "password": "newpassword@99A",
        "name": "New",
        "last_name": "User",
        "age": 30,
        "role_id": "6781177cf2e31cc2c6b2b7fb" 
    }

    mock_user_collection.insert_one.return_value = MagicMock(inserted_id="12345")

    response = client.post(
        "/api/v1/users/create/user",
        json=user_data
    )

    assert response.status_code == 401


def test_create_user_ivalid_login(client,access_token_admin,mock_user_collection):
    user_data = {
        "login": "newuser",
        "password": "newpassword@99A",
        "name": "New",
        "last_name": "User",
        "age": 30,
        "role_id": "6781177cf2e31cc2c6b2b7fb" 
    }

    mock_user_collection.insert_one.return_value = MagicMock(inserted_id="12345")

    response = client.post(
        "/api/v1/users/create/user",
        json=user_data,  
        cookies={"access_token": access_token_admin} 
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "This login already exists"}