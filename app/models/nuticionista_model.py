from sqlalchemy import Column, Integer, String, Date

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from ..ext.db import db
from ..ext.flask_login import login_manager

@login_manager.user_loader
def get_user(user_id):
    return Nutricionista.query.filter_by(id=user_id).first()

class Nutricionista(db.Model, UserMixin):
    __tablename__ = "nutricionista"

    id = Column(Integer, primary_key=True)
    email = Column(String(length=60), unique=True)
    full_name = Column(String(length=60))
    birt_date = Column(Date)
    cnpj = Column(String(length=11))
    password_hash = Column(String(length=256))

    clientes = db.relationship("Cliente", backref="nutricionista", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)