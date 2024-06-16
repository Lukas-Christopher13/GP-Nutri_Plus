from . import auth

from flask import redirect

from flask_login import login_required, logout_user

@login_required
@auth.route("/logout")
def logout():
    logout_user()
    return redirect("/")