from tests.base import client,access_token_user,mock_user_collection

def test_get_users(client,access_token_user):

    response = client.get("/api/v1/users/get/users", cookies={"access_token": access_token_user} )

    assert response.status_code == 200

def test_get_user_id(client,access_token_user):
    user_data = {
        "id": "67866b7afdcec5bdc22760b3"
    }

    response = client.get(f"/api/v1/users/get/{user_data["id"]}", cookies={"access_token": access_token_user} )

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == user_data["id"]