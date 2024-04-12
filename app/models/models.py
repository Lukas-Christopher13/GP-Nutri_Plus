from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_paciente = db.Column(db.String(100), nullable=False)
    resultado = db.Column(db.Text, nullable=False)
    arquivo = db.Column(db.String(255), nullable=False)  # Nome do arquivo PDF
    data_envio = db.Column(db.DateTime, default=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()
