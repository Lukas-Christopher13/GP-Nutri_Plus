from . import auth

from flask import render_template, flash, url_for, redirect, request

from ...forms.auth.reset_password_form import ResetPasswordForm

@auth.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    form = ResetPasswordForm(request.form)

    if form.validate():
        flash("O requisição realizada. Verifique a caixa de entrada do seu email")
        
        return redirect(url_for("auth.login"))
        
    return render_template("auth/forgot_password.html", form=form)