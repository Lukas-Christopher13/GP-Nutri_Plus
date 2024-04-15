from utils import create_user


def test_login_user(client):
    create_user()

    response = client.post("/login", data={
        "email": "test@gmail.com",
        "password": "test1234"
    })

    assert response.status_code == 200

    

