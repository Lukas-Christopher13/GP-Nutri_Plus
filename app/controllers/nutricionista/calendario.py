from . import nutricionista

from flask import render_template, redirect, url_for

from flask_login import login_required

from ...repository.consulta_repository import ConsultaRepository
from ...services.agendar_consulta_service import ConsultaService

@nutricionista.route("/calendario")
@login_required
def visualizar_calendario():
    consulta_repository = ConsultaRepository()
    consulta_service = ConsultaService(consulta_repository)

    return render_template("nutricionista/calendario.html", calendars=consulta_service.calendar_list)

@nutricionista.route("/confirmar_consulta/<date>")
@login_required
def confirmar_consulta(date):
    consulta_repository = ConsultaRepository()
    consulta_repository.update_status(date, "Consulta Confirmada")
        
    return redirect(url_for("nutricionista.visualizar_calendario"))


    

