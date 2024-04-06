# app.py

from flask import Flask
from app.ext.db import db
from app.models import *
from app.controllers import *
from app.controllers.diet.diet_controller import diet_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'mysecretkey'
db.init_app(app)

# Registrar blueprints
app.register_blueprint(diet_bp)

if __name__ == '__main__':
    app.run(debug=True)
