from ..ext.db import db
from ..models.cliente_model import Cliente

class ClienteRepository:
    def create_cliente(self, cliente: Cliente):
        db.session.add(cliente)
        db.session.commit()
