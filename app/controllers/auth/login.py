from . import auth

from flask import render_template, redirect, url_for, request

from flask_login import login_user

from ...forms.auth.login_form import LoginForm
from ...models.cliente_model  import Cliente
from ...models.nuticionista_model import Nutricionista

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
       
    if request.method == "POST" and form.validate():

        #alterar para função que faz tanto para Nutri quanto pra cliente
        cliente: Cliente = Cliente.query.filter_by(email=form.email.data).first()
        nutricionista: Nutricionista = Nutricionista.query.filter_by(email=form.email.data).first()

        if nutricionista is not None and nutricionista.check_password(form.password.data):
            login_user(nutricionista)
            return redirect(url_for("home.nutricionista_home_page"))
        
        if cliente is not None and cliente.check_password(form.password.data):
            login_user(cliente)
            return redirect(url_for("home.cliente_home_page"))

        return redirect("/login")

    return render_template("/auth/login.html", form=form)