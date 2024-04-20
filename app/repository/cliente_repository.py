from ..ext.db import db
from ..models.cliente_model import Cliente

class ClienteRepository:
    def insert(self, cliente: Cliente):
        db.session.add(cliente)
        db.session.commit()
        return True
    
    def email_already_exists(self, email):
        result = Cliente.query.filter(Cliente.email == email).first()
        
        if result is None:
            return False
        
        return True
