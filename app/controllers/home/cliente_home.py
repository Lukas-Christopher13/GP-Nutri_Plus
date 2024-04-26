from . import home

from flask import render_template

from flask_login import login_required, current_user

@home.route("/cliente_home_page")
@login_required
def cliente_home_page():
    name = current_user.full_name
    return render_template("home/cliente_home.html", name=name)