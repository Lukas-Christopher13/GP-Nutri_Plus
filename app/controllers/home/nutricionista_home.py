from . import home

from flask import render_template

from flask_login import login_required, current_user

@home.route("/nutricionista_home_page")
@login_required
def nutricionista_home_page():
    name = current_user.full_name
    return render_template("home/nutricionista_home.html", name=name)