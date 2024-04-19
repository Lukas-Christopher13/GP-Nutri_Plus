from ..ext.db import db
from ..models.nuticionista_model import Nutricionista

class NutricionistaRepository:
    def insert(self, nutricionista: Nutricionista):
        db.session.add(nutricionista)
        db.session.commit()
        return True
