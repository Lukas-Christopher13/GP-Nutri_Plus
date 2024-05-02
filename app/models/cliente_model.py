from datetime import datetime
from datetime import timedelta

from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from ..ext.db import db
from ..ext.flask_login import login_manager

@login_manager.user_loader
def get_user(user_id):
    return Cliente.query.filter_by(id=user_id).first()

class Cliente(db.Model, UserMixin):
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

    login_attempts = Column(Integer, default=0, nullable=False)
    block_duration = Column(DateTime, default=datetime.now())

    consulta = db.relationship("Consulta", backref="cliente", lazy=True)

    nutricionista_id = Column(Integer, ForeignKey("nutricionista.id"), nullable= False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def increase_login_attempts(self):
        if self.login_attempts >= 3:
            self.block_user()
        
        self.login_attempts+= 1

    def block_user(self):
        time_now = datetime.now()
        self.block_duration = time_now + timedelta(minutes=1)

        db.session.commit()

    def is_blocked(self):
        if self.block_duration > datetime.now():
            return True
        return False