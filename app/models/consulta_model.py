from sqlalchemy import Column, Date, String, Integer, ForeignKey

from ..ext.db import db
from ..ext.flask_login import login_manager

#adiconar campo motivo
class Consulta(db.Model):
    __tablename__ = "consulta"

    date = Column(Date, primary_key=True)
    time = Column(String, primary_key=True)
    status = Column(String(32), nullable=False)

    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)
