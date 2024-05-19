from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import atexit
from ..repository.consulta_repository import ConsultaRepository

consulta_repository = ConsultaRepository()
mail = Mail()

def enviar_lembrete_consulta(app):
    with app.app_context():
        agora = datetime.now()
        lembrete_time = agora + timedelta(hours=24)
        consultas = consulta_repository.get_all_between(agora, lembrete_time)

        for consulta in consultas:
            cliente = cliente.consulta
            if cliente.email:
                msg = Message(
                    subject="Lembrete de Consulta",
                    recipients=[cliente.email],
                    body=f"Olá {cliente.nome},\n\nLembrete: você tem uma consulta agendada para {consulta.date} às {consulta.time}.\n\nAtenciosamente,\nEquipe de Nutricionistas"
                )
                mail.send(msg)

scheduler = BackgroundScheduler()

def init_scheduler(app):
    mail.init_app(app)
    scheduler.add_job(func=lambda: enviar_lembrete_consulta(app), trigger='interval', hours=1)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())
