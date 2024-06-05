from . import auth

from flask import render_template, redirect, url_for, flash, request

from ...forms.auth.login_form import LoginForm, LoginADMForm, RegisterDeviceForm
from ...models.nuticionista_model import Nutricionista
from ...models.dispositivos import Dispositivo

@auth.route("/adm_login", methods=["GET", "POST"])
def adm_login():
    form = LoginADMForm(request.form)

    if form.validate():

        if form.email.data != "adm@gmail.com":
            message = "Email invalido"
            return render_template("auth/adm_login.html", form=form, message=message)
        
        if form.password.data != "teste123":
            message = "Senha invalida"
            return render_template("auth/adm_login.html", form=form, message=message)
        
        return redirect(url_for("auth.register_device"))
        
    return render_template("auth/adm_login.html", form=form)

@auth.route("/register_device", methods=["GET", "POST"])
def register_device():
    form = RegisterDeviceForm (request.form)

    if form.validate():
        nutricionista = Nutricionista.query.filter_by(email=form.email.data).first()

        if nutricionista is None:
            message = "Esse usuário não existe"
            return render_template("auth/register_device.html", form=form, message=message)

        Dispositivo.register_divice(request, nutricionista)

        flash("Dispositivo cadastrado")
        
        return redirect(url_for("auth.login"))
    
    return render_template("auth/register_device.html", form=form)
