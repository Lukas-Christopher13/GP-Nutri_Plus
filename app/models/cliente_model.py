from sqlalchemy import Column, Integer, String, Date

from werkzeug.security import generate_password_hash, check_password_hash

from ..ext.db import db

class Cliente(db.Model):
    __tablename__ = "cliente"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(length=60), unique=True)
    full_name = Column(String(length=60))
    birt_date = Column(Date)
    cpf = Column(String(length=11))
    country = Column(String(length=30))
    state = Column(String(length=30))
    city = Column(String(length=30))
    password_hash = Column(String(length=256))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
