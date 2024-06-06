from app.utils.sms import send_sms
from . import nutricionista

from flask import current_app, render_template, redirect, url_for

from flask_login import login_required

from ...repository.consulta_repository import ConsultaRepository
from ...services.agendar_consulta_service import ConsultaService

@nutricionista.route("/calendario")
@login_required
def visualizar_calendario():
    consulta_repository = ConsultaRepository()
    consulta_service = ConsultaService(consulta_repository)

    return render_template("nutricionista/calendario.html", calendars=consulta_service.calendar_list)

@nutricionista.route("/confirmar_consulta/<date>/<time>")
@login_required
def confirmar_consulta(date, time):
    consulta_repository = ConsultaRepository()
    consulta_repository.update_status(date, time, "Consulta Confirmada")

    # Enviar SMS ao cliente
    sms_body = f"Sua consulta foi CONFIRMADA para {date} às {time}."
    client_phone_number = current_app.config['CLIENT_PHONE_NUMBER']
    send_sms(client_phone_number, sms_body)

        
    return redirect(url_for("nutricionista.visualizar_calendario"))

@nutricionista.route("/cancelar_consulta/<date>/<time>")
@login_required
def cancelar_consulta(date, time):
    consulta_repository = ConsultaRepository()
    consulta_repository.update_status(date, time, "Consulta Cancelada")
        
    return redirect(url_for("nutricionista.visualizar_calendario"))
