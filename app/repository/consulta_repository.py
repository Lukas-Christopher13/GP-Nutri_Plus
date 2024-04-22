from ..ext.db import db
from ..models.consulta_model import Consulta


class ConsultaRepository:
    def insert(self, consulta: Consulta):
        db.session.add(consulta)
        db.session.commit()