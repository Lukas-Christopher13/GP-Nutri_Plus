import pytest
import datetime

from unittest.mock import MagicMock

from app import create_app
from app.ext.db import db

from app.repository.nutricionista_repository import NutricionistaRepository

@pytest.fixture()
def app():
    app = create_app("test")
    
    with app.app_context():
        db.create_all()
    # other setup can go here

    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

@pytest.fixture()
def nutricionista_mocked():
    nutricionista = MagicMock()

    nutricionista.id = 1
    nutricionista.email = "test@gmail.com"
    nutricionista.full_name = "nutricionista test"
    nutricionista.birt_date = datetime.date.today()
    nutricionista.cnpj = "12345678901"
    nutricionista.password = "teste123"

    return nutricionista

@pytest.fixture()
def cliente_mocked():
    cliente = MagicMock()

    cliente.id = 1 
    cliente.email = "test@gmail.com"
    cliente.full_name = "nutricionista test"
    cliente.birt_date = datetime.date.today()
    cliente.cpf = "12345678901"
    cliente.contry = "Brazil" 
    cliente.state = "Paraíba"
    cliente.city = "Campina Grande"
    cliente.password_hash = "akfjsadlkjflaçlsdjfl30820"

    return cliente