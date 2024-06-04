from . import cliente

from flask import render_template

from flask_login import login_required, current_user

from ...models.consulta_model import Consulta


@cliente.route("/historico")
@login_required
def historico():

    consultas = Consulta.query.filter_by(cliente_id = current_user.id).all()

    return render_template("cliente/historico.html", consultas=consultas)