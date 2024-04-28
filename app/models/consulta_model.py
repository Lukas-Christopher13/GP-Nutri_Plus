from sqlalchemy import Column, Date, String, Integer, ForeignKey

from ..ext.db import db
from ..ext.flask_login import login_manager

from ..models.cliente_model import Cliente
from ..repository.cliente_repository import ClienteRepository

#adiconar campo motivo
class Consulta(db.Model):
    __tablename__ = "consulta"

    date = Column(Date, primary_key=True)
    time = Column(String, primary_key=True)
    status = Column(String(32), nullable=False)
    motivo = Column(String(255))

    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)

    def cliente_info(self):
        return f"{self.time} | {self.status} | HORÁRIO AGENDADO!"
    
    def nutricionista_info(self):
        cliente_repository = ClienteRepository()
        cliente: Cliente = cliente_repository.get_cliente_by_id(self.cliente_id)
        return f"Cliente: {cliente.full_name} | Horario: {self.time} H | Status: {self.status}"