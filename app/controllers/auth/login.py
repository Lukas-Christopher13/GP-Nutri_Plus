from . import auth

from flask import render_template, redirect, url_for, request

from flask_login import login_user

from ...forms.auth.login_form import LoginForm
from ...models.nuticionista_model import Nutricionista

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
       
    if request.method == "POST" and form.validate():

        #alterar para função que faz tanto para Nutri quanto pra cliente
        nutri: Nutricionista = Nutricionista.query.filter_by(email=form.email.data).first()

        if not nutri or not nutri.check_password(form.password.data):
            return redirect(url_for("login"))
        
        login_user(nutri)
        
        return redirect("/")

    return render_template("/auth/login.html", form=form)