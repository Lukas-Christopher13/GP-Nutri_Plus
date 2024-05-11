from . import auth

from flask import render_template, request

from ...forms.auth.reset_password_form import ResetPasswordForm

@auth.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    form = ResetPasswordForm(request.form)

    return render_template("auth/forgot_password.html", form=form)