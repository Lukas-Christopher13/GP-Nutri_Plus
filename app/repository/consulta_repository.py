from ..ext.db import db
from ..models.consulta_model import Consulta
from datetime import datetime



class ConsultaRepository:
    def insert(self, consulta: Consulta):
        db.session.add(consulta)
        db.session.commit()

    def time_already_scheduled(self, date_, time_):
        consulta : Consulta = Consulta.query.filter_by(date=date_, time=time_).first()

        if consulta is None:
            return False
        
        return True
    
    def get_all_by_date(self, date_):
        return Consulta.query.filter_by(date=date_).all()
    
    def update(self, consulta: Consulta):
        db.session.commit()

    def update_status(self, date_, time_, status):
        consulta : Consulta = Consulta.query.filter_by(date=date_, time=time_).first()

        consulta.status = status

        db.session.commit()
        
    def get_all_between(self, start_time: datetime, end_time: datetime):
        return Consulta.query.filter(Consulta.date.between(start_time, end_time)).all()
