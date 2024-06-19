from apscheduler.schedulers.background import BackgroundScheduler
from flask_login import current_user
from ..models.consulta_model import Consulta
from ..utils.sms import send_sms
from datetime import datetime, timedelta
from flask import current_app
from ..ext.db import db

def send_reminder():
    with current_app.app_context():
        tomorrow = datetime.now() + timedelta(days=1)
        consultas = Consulta.query.filter(
            Consulta.date == tomorrow.date(),
            Consulta.time - datetime.now().time() < timedelta(hours=24).total_seconds()
        ).all()
        for consulta in consultas:
            date = consulta.date
            time = consulta.time.strftime('%H:%M')
            sms_body = f"Sua consulta foi agendada para {date.strftime('%d/%m/%Y')} às {time}."
            client_phone_number = current_app.config['CLIENT_PHONE_NUMBER']
            send_sms(client_phone_number.phone_number, sms_body)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=send_reminder, trigger="interval", hours=24)
    scheduler.start()
