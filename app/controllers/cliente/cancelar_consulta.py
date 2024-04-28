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

@cliente.route("/cancelar_consulta/<int:consulta_id>", methods=["GET"])
@login_required
def cancelar_consulta(consulta_id):
    consultaRepository = ConsultaRepository()
    consulta = consultaRepository.get_by_id(consulta_id)

    if not consulta or consulta.cliente_id != current_user.id:
        flash("Consulta não encontrada ou não autorizada", "error")
        return redirect(url_for("cliente.agendar_consulta"))

    if consulta.status == "Cancelado":
        flash("Esta consulta já foi cancelada", "info")
        return redirect(url_for("cliente.agendar_consulta"))

    consulta.status = "Cancelado"
    consultaRepository.update(consulta)

    flash("Consulta cancelada com sucesso!", "success")
    return redirect(url_for("cliente.agendar_consulta"))
