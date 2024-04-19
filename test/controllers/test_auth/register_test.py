import datetime

from app.ext.db import db

from app.models.cliente_model import Cliente
from app.models.nuticionista_model import Nutricionista


VALID_USER = {
    "email": "test@gmail.com",
    "full_name": "nutricionista test",
    "birt_date": datetime.date.today(),
    "cpf": "12345678901",
    "country": "test-----",
    "state": "test-----",
    "city": "test-----",
    "password": "test1234",
    "confirm_password": "test1234"
}

VALID_NUTRI = {
    "email": "test@gmail.com",
    "full_name": "nutricionista test",
    "birt_date": datetime.date.today(),
    "cnpj": "12345678901",
    "password": "test1234",
    "confirm_password": "test1234"
}

def test_register(client, app):
    response = client.post("/register", data=VALID_USER)

    with app.app_context():
        cliente: Cliente = Cliente.query.filter_by(email=VALID_USER["email"]).first()

    assert cliente.email == VALID_USER["email"]
  
def test_register_nutricionista(client, app):
    response = client.post("/register-nutricionista", data=VALID_NUTRI)

    with app.app_context():
        nutricionista: Nutricionista = Nutricionista.query.filter_by(email=VALID_NUTRI["email"]).first()
    
    assert nutricionista.email == VALID_NUTRI["email"]
