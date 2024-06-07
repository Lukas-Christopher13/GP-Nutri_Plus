from datetime import datetime, timedelta
from ..ext.db import db
from ..models.consulta_model import Consulta
from ..models.models import Diet
from ..models.models import Activity
from ..models.models import Exam
from apscheduler.schedulers.background import BackgroundScheduler



def purge_dados(model, date_column, retention_days):
    differences = datetime.utcnow() - timedelta(days=retention_days)
    old_records = db.session.query(model).filter(date_column < differences).all()
    
    for record in old_records:
        db.session.delete(record)
    
    db.session.commit()
    
    print(f"{len(old_records)} registros antigos foram purgados da tabela {model.__tablename__}.")

def exec():
    retention_days = 365
    purge_dados(Consulta, Consulta.date, retention_days)
    purge_dados(Diet, Diet.date, retention_days)
    purge_dados(Activity, Activity.date, retention_days)
    purge_dados(Exam, Exam.date, retention_days)

def init_purge_sheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=exec, trigger="interval", days=1)
    scheduler.start()

