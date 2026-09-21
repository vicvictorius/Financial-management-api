def create_user(client, username="victor", email="victor@test.com"):
    response = client.post(
        "/auth/register",
        json={
            "username": username,
            "email": email,
            "password": "123456",
        },
    )

    assert response.status_code == 200


def get_token(client, username="victor"):
    response = client.post(
        "/auth/login",
        data={
            "username": username,
            "password": "123456",
        },
    )

    assert response.status_code == 200

    return response.json()["access_token"]


def create_category(client, token):
    response = client.post(
        "/categories/",
        json={"name": "Salary"},
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code in (200, 201)

    return response.json()["id"]


def create_transaction(client, token, category_id):
    response = client.post(
        "/transactions/",
        json={
            "description": "Monthly salary",
            "amount": "5000.00",
            "type": "income",
            "category_id": category_id,
        },
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 201

    return response.json()


def test_create_transaction(client):
    create_user(client)

    token = get_token(client)
    category_id = create_category(client, token)

    transaction = create_transaction(client, token, category_id)

    assert transaction["description"] == "Monthly salary"
    assert transaction["amount"] == "5000.00"
    assert transaction["type"] == "income"
    assert transaction["category_id"] == category_id


def test_list_transactions(client):
    create_user(client)

    token = get_token(client)
    category_id = create_category(client, token)

    create_transaction(client, token, category_id)

    response = client.get(
        "/transactions/",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200

    transactions = response.json()

    assert len(transactions) == 1
    assert transactions[0]["description"] == "Monthly salary"


def test_get_transaction_by_id(client):
    create_user(client)

    token = get_token(client)
    category_id = create_category(client, token)

    transaction = create_transaction(client, token, category_id)

    response = client.get(
        f"/transactions/{transaction['id']}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json()["id"] == transaction["id"]


def test_update_transaction(client):
    create_user(client)

    token = get_token(client)
    category_id = create_category(client, token)

    transaction = create_transaction(client, token, category_id)

    response = client.put(
        f"/transactions/{transaction['id']}",
        json={
            "description": "Updated salary",
            "amount": "5500.00",
        },
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200

    updated = response.json()

    assert updated["description"] == "Updated salary"
    assert updated["amount"] == "5500.00"


def test_delete_transaction(client):
    create_user(client)

    token = get_token(client)
    category_id = create_category(client, token)

    transaction = create_transaction(client, token, category_id)

    response = client.delete(
        f"/transactions/{transaction['id']}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 204

    response = client.get(
        f"/transactions/{transaction['id']}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 404


def test_transactions_require_authentication(client):
    response = client.get("/transactions/")

    assert response.status_code == 401


def test_user_cannot_access_another_users_transaction(client):
    create_user(client, "victor", "victor@test.com")

    token_victor = get_token(client, "victor")
    category_id = create_category(client, token_victor)

    transaction = create_transaction(
        client,
        token_victor,
        category_id,
    )

    create_user(
        client,
        "other_user",
        "other@test.com",
    )

    token_other = get_token(client, "other_user")

    response = client.get(
        f"/transactions/{transaction['id']}",
        headers={"Authorization": f"Bearer {token_other}"},
    )

    assert response.status_code == 404
