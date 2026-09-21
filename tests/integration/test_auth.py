def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "username": "victor",
            "email": "victor@test.com",
            "password": "123456",
        },
    )

    assert response.status_code == 200


def test_login_user(client):
    client.post(
        "/auth/register",
        json={
            "username": "victor",
            "email": "victor@test.com",
            "password": "123456",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "victor",
            "password": "123456",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_password(client):
    client.post(
        "/auth/register",
        json={
            "username": "victor",
            "email": "victor@test.com",
            "password": "123456",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "victor",
            "password": "senha_errada",
        },
    )

    assert response.status_code == 401


def test_login_nonexistent_user(client):
    response = client.post(
        "/auth/login",
        data={
            "username": "usuario_inexistente",
            "password": "123456",
        },
    )

    assert response.status_code == 401


def test_valid_jwt(client):
    client.post(
        "/auth/register",
        json={
            "username": "victor",
            "email": "victor@test.com",
            "password": "123456",
        },
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "victor",
            "password": "123456",
        },
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/dashboard/summary",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200


def test_invalid_jwt(client):
    response = client.get(
        "/dashboard/summary",
        headers={"Authorization": "Bearer token_invalido"},
    )

    assert response.status_code == 401

def test_register_duplicate_username(client):
    client.post(
        "/auth/register",
        json={
            "username": "victor",
            "email": "victor@test.com",
            "password": "123456",
        },
    )

    response = client.post(
        "/auth/register",
        json={
            "username": "victor",
            "email": "outro@test.com",
            "password": "123456",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Username or email already exists"


def test_register_duplicate_email(client):
    client.post(
        "/auth/register",
        json={
            "username": "victor",
            "email": "victor@test.com",
            "password": "123456",
        },
    )

    response = client.post(
        "/auth/register",
        json={
            "username": "outro",
            "email": "victor@test.com",
            "password": "123456",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Username or email already exists"
