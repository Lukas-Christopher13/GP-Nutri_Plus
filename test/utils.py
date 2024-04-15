import datetime

from app.ext.db import db
from app.models.cliente_model import Cliente

def create_user():
    cliente = Cliente(
        email="test@gmail.com",
        full_name="nutricionista test",
        birt_date= datetime.date.today(),
        cpf="12345678901",
        country="test-----",
        state="test-----",
        city="test-----",
    )

    cliente.set_password("test123")

    db.session.add(cliente)
    db.session.commit()


    