from datetime import datetime, timedelta
from ..ext.db import db
from ..models.consulta_model import Consulta
from ..models.models import Diet
from ..models.models import Activity
from ..models.models import Exam
from apscheduler.schedulers.background import BackgroundScheduler



def purge_old_records(model, date_column, retention_days):
    cutoff_date = datetime.utcnow() - timedelta(days=retention_days)
    old_records = db.session.query(model).filter(date_column < cutoff_date).all()
    
    for record in old_records:
        db.session.delete(record)
    
    db.session.commit()
    
    print(f"{len(old_records)} registros antigos foram purgados da tabela {model.__tablename__}.")

def purge_all_old_records():
    retention_days = 365
    purge_old_records(Consulta, Consulta.date, retention_days)
    purge_old_records(Diet, Diet.date, retention_days)
    purge_old_records(Activity, Activity.date, retention_days)
    purge_old_records(Exam, Exam.date, retention_days)

def init_purge_sheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=purge_all_old_records, trigger="interval", days=1)
    scheduler.start()

