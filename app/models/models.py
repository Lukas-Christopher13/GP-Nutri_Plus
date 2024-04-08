
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

