from app import create_app
from app.ext.db import db

from app.models.models import Food, Exam, Diet

from app.models.cliente_model import Cliente
from app.models.consulta_model import Consulta
from app.models.nuticionista_model import Nutricionista

from app.controllers import *

app = create_app("develop")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)



