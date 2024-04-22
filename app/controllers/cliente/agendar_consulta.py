from . import cliente

from flask_login import login_required
from flask import render_template, request

from ...forms.cliente.agendar_consulta_form import AgendarConsultaForm

@cliente.route("/agendar_consulta")
@login_required
def agendar_consulta():
    form = AgendarConsultaForm(request.form)
    return render_template("cliente/agendar_consulta.html", form=form)
    