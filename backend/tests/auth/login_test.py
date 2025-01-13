from tests.base import client, mock_user_collection


def test_successful_login(client, mock_user_collection):
    user_data = {
        "_id": "12345",
        "login": "testuser",
        "password": "hashedpassword",
    }

    mock_user_collection.find_one.return_value = user_data

    response = client.post(
        "api/v1/auth/login",
        json={"login": "admin", "password": "Admin888@"}
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Login successful"}
    assert "access_token" in response.cookies

def test_invalid_login_credentials(client, mock_user_collection):
    mock_user_collection.find_one.return_value = None

    response = client.post(
        "api/v1/auth/login",
        json={"login": "invaliduser", "password": "wrongpassword"}
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid login credentials"}

def test_invalid_password(client, mock_user_collection):
    user_data = {
        "_id": "12345",
        "login": "testuser",
        "password": "hashedpassword",
    }

    mock_user_collection.find_one.return_value = user_data

    response = client.post(
        "api/v1/auth/login",
        json={"login": "testuser", "password": "wrongpassword"}
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid login credentials"}

