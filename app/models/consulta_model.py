from sqlalchemy import Column, Date, String, Integer, ForeignKey

from ..ext.db import db
from ..ext.flask_login import login_manager


class Consulta(db.Model):
    __tablename__ = "consulta"

    data = Column(Date, primary_key=True)
    time = Column(String, primary_key=True)
    status = Column(String, nullable=False)

    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)
