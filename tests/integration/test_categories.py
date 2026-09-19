def create_user(client):

    response = client.post(
        "/auth/register",
        json={"username": "victor", "email": "victor@test.com", "password": "123456"},
    )

    assert response.status_code == 200


def get_token(client):

    response = client.post("/auth/login", data={"username": "victor", "password": "123456"})

    return response.json()["access_token"]


def test_create_category(client):

    create_user(client)

    token = get_token(client)

    response = client.post(
        "/categories/", json={"name": "Alimentação"}, headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
