from . import cliente

from flask import render_template

from flask_login import login_required, current_user

from ...models.models import Diet
from ...models.consulta_model import Consulta


@cliente.route("/historico")
@login_required
def historico():

    dietas = Diet.query.filter_by(cliente_id = current_user.id).all()
    consultas = Consulta.query.filter_by(cliente_id = current_user.id).all()

    return render_template("cliente/historico.html", consultas=consultas, dietas=dietas)