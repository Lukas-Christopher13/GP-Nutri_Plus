from . import nutricionista

from flask import render_template, request

from flask_login import login_required, current_user

from ...models.cliente_model import Cliente
from ...models.nuticionista_model import Nutricionista

@nutricionista.route("/monitorar_paciente")
@login_required
def monitorar_paciente():

    clientes = Cliente.query.all()

    show_data = request.args.get("data")

    if show_data:
        cliente_id = show_data

        
        return render_template("nutricionista/monitorar_paciente.html", clientes=clientes)
    
    return render_template("nutricionista/monitorar_paciente.html", clientes=clientes)
    
    