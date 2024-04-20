from . import home

from flask import render_template

from flask_login import login_required

@home.route("/cliente_home_page")
#@login_required
def cliente_home_page():
    return render_template("home/cliente_home.html")