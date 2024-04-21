from ..ext.db import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


class Diet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    objective = db.Column(db.String(200))
    restrictions = db.Column(db.String(200))
    duration = db.Column(db.Integer)  

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    diet_id = db.Column(db.Integer, db.ForeignKey('diet.id'), nullable=False)
    diet = db.relationship('Diet', backref=db.backref('foods', lazy=True))

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_paciente = db.Column(db.String(100), nullable=False)
    resultado = db.Column(db.Text, nullable=False)
    arquivo = db.Column(db.String(255), nullable=False)  # Nome do arquivo PDF
    data_envio = db.Column(db.DateTime, default=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()
