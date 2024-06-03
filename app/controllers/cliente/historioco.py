from . import cliente

from flask import render_template

@cliente.route("/historico")
def historico():
    



    return render_template("cliente/historico.html")