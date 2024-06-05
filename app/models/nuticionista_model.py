import uuid

from datetime import datetime
from datetime import timedelta

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Boolean

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from ..ext.db import db
from ..ext.flask_login import login_manager
from ..models.cliente_model import Cliente
from ..models.dispositivos import Dispositivo

@login_manager.user_loader
def get_user(user_id):
    cliente = Cliente.query.filter_by(id=user_id).first()
    nutricionista = Nutricionista.query.filter_by(id=user_id).first()

    if cliente is not None:
        return cliente

    return nutricionista

class Nutricionista(db.Model, UserMixin):
    __tablename__ = "nutricionista"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(length=60), unique=True)
    full_name = Column(String(length=60))
    birt_date = Column(Date)
    cnpj = Column(String(length=11))
    password_hash = Column(String(length=256))

    login_attempts = Column(Integer, default=0, nullable=False)
    block_duration = Column(DateTime, default=datetime.now())

    clientes = db.relationship("Cliente", backref="nutricionista", lazy=True)
    notifications = db.relationship("Notification", backref="nutricionista", lazy=True)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
    
    def increase_login_attempts(self):
        if self.login_attempts >= 3:
            self.block_user()
        else:
            self.login_attempts+= 1
            db.session.commit()

    def block_user(self):
        time_now = datetime.now()
        self.block_duration = time_now + timedelta(minutes=1)

        db.session.commit()

    def is_blocked(self):
        if self.block_duration > datetime.now():
            return True
        return False
    
    def update_login_attempts(self):
        self.login_attempts = 0
        self.block_duration = datetime.now()
        db.session.commit()

    def is_device(self, divice : Dispositivo):
        dispositivos = Dispositivo.query.filter_by(nutricionista_id = self.id).all()

        for dispositivo in dispositivos:
            if dispositivo == divice:
                return True
        return False

class Notification(db.Model):
    id = Column(Integer, primary_key=True)
    message = Column(String(255), nullable=False)
    read = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    nutricionista_id = Column(Integer, ForeignKey('nutricionista.id'), nullable=False)    
    
