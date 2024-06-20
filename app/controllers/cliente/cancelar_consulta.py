from . import cliente

from datetime import datetime

from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from ...models.consulta_model import Consulta
from ...repository.consulta_repository import ConsultaRepository
from ...services.agendar_consulta_service import ConsultaService
from ...forms.cliente.agendar_consulta_form import AgendarConsultaForm


from . import cliente
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from ...models.consulta_model import Consulta
from ...repository.consulta_repository import ConsultaRepository
from ...utils.notifications.remacacao_de_consulta import notificar

@cliente.route("/cancelar_consulta/<consulta_date>/<consulta_time>", methods=["GET"])
@login_required
def cancelar_consulta(consulta_date, consulta_time):
    consultaRepository = ConsultaRepository()
    consultas = consultaRepository.get_all_by_date(consulta_date)

    consulta_a_cancelar = None
    for consulta in consultas:
        if consulta.time == consulta_time:
            consulta_a_cancelar = consulta
            break

    if not consulta_a_cancelar or consulta_a_cancelar.cliente_id != current_user.id:
        flash("Consulta não encontrada ou não autorizada", "error")
        return redirect(url_for("cliente.agendar_consulta"))

    consulta_a_cancelar.status = "Cancelado"  
    consultaRepository.update(consulta_a_cancelar)

    message = f"O cliente {current_user.full_name} deseja remarcar a data de sua consulta!"
    notificar(current_user, message)

    
    return redirect(url_for("cliente.agendar_consulta"))

