new_user = {
    "appid": 101,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "cluster": "CLUSTER_1"
}

def test_create_user(client):
    response = client.post("/users/", json=new_user)
    assert response.status_code == 201, f"Unexpected response: {response.text}"
    data = response.get_json()
    assert data["appid"] == new_user["appid"]
    assert data["name"] == new_user["name"]
    assert data["email"] == new_user["email"]
    assert data["cluster"] == new_user["cluster"]

def test_get_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    users = response.get_json()
    assert isinstance(users, list)
    assert any(user["appid"] == new_user["appid"] for user in users)
