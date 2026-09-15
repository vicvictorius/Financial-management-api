def create_user(client):

    response = client.post(
        "/auth/register",
        json={
            "username": "victor",
            "email": "victor@test.com",
            "password": "123456"
        }
    )

    assert response.status_code == 200


def get_token(client):

    response = client.post(
        "/auth/login",
        data={
            "username": "victor",
            "password": "123456"
        }
    )

    return response.json()["access_token"]


def test_dashboard_summary(client):

    create_user(client)

    token = get_token(client)

    response = client.get(
        "/dashboard/summary",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "total_income" in data
    assert "total_expenses" in data
    assert "balance" in data


def test_dashboard_monthly(client):

    create_user(client)

    token = get_token(client)

    response = client.get(
        "/dashboard/monthly",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    assert isinstance(response.json(), dict)


def test_dashboard_requires_authentication(client):

    response = client.get(
        "/dashboard/summary"
    )

    assert response.status_code == 401


def test_monthly_dashboard_requires_authentication(client):

    response = client.get(
        "/dashboard/monthly"
    )

    assert response.status_code == 401