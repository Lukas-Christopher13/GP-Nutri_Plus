from . import auth

from flask import render_template, flash, url_for, redirect, request

from flask_mail import Message

from ...forms.auth.reset_password_form import ResetPasswordForm, SetNewPasswordForm

from ...models.cliente_model import Cliente
from ...models.nuticionista_model import Nutricionista

from ...ext.db import db
from ...ext.mail import mail

@auth.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    form = ResetPasswordForm(request.form)

    #se o cliente não existir da erro!
    if form.validate():
        user = get_user_by_email(form.email.data)

        if user is None:
            message = "Email invalido! Esse usuário não possui cadastro!"
            return render_template("auth/forgot_password.html", form=form, message=message)

        try_send_email(user)
        flash("A requisição foi realizada. Verifique a caixa de entrada do seu email")
        
        return redirect(url_for("auth.login"))
        
    return render_template("auth/forgot_password.html", form=form)

def get_user_by_email(email):
    user = Cliente.query.filter(Cliente.email == email).first()
    
    if user is None:
        user = Nutricionista.query.filter(Nutricionista.email == email).first()
    
    return user
    
def try_send_email(user):
    try:
        send_email(user)
    except:
        pass

def send_email(user):
    token = user.get_token()
    msg = Message("Password Reset Request", recipients=[user.email], sender="nutriplus2024@gmail.com")
    msg.body = f"""
    Clique no link para fazer o reset do seu password:
    
    ---> {url_for("auth.reset_token", token=token, _external=True)}

    """
    mail.send(msg)

@auth.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_token(token):
    user : Cliente = Cliente.verify_token(token)

    if user is None:
        flash("Esse token é invalido ou expirou!")
        return redirect(url_for("auth.login"))
    
    form = SetNewPasswordForm(request.form)
    if form.validate():
        user.set_password(form.password.data)
        db.session.commit()

        flash("O password foi alterado! Faça o login!")
        return redirect(url_for("auth.login"))
    
    return render_template("chage_password.html", form=form)