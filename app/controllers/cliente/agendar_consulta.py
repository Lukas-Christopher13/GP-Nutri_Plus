from . import cliente

from flask import render_template, request
from flask_login import login_required, current_user

from ...models.consulta_model import Consulta
from ...repository.consulta_repository import ConsultaRepository
from ...forms.cliente.agendar_consulta_form import AgendarConsultaForm

@cliente.route("/agendar_consulta", methods=["GET", "POST"])
@login_required
def agendar_consulta():
    form = AgendarConsultaForm(request.form)
    consultaRepository = ConsultaRepository()

    if request.method == "POST" and form.validate():
        time = form.time.data[0]

        consulta = Consulta(
            date=form.date.data,
            time=time,
            status="Agendado",
            cliente_id=current_user.id
        )

        consultaRepository.insert(consulta)

        return render_template("cliente/agendar_consulta.html", form=form)

    return render_template("cliente/agendar_consulta.html", form=form)
    