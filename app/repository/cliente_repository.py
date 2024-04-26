from ..ext.db import db
from ..models.cliente_model import Cliente

class ClienteRepository:
    def create_cliente(self, cliente: Cliente):
        db.session.add(cliente)
        db.session.commit()

    def get_cliente_by_id(sefl, id: int) -> Cliente:
        cliente: Cliente = Cliente.query.filter(Cliente.id==id).first()
        return cliente
