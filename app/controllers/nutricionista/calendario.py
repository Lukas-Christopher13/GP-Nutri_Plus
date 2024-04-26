from . import nutricionista

from flask import render_template

from flask_login import login_required

from ...repository.consulta_repository import ConsultaRepository
from ...services.agendar_consulta_service import ConsultaService

@nutricionista.route("/calendario")
@login_required
def visualizar_calendario():
    consulta_repository = ConsultaRepository()
    consulta_service = ConsultaService(consulta_repository)

    return render_template("nutricionista/calendario.html", calendars=consulta_service.calendar_list)


    

