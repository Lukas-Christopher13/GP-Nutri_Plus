from . import home

from flask import render_template

from flask_login import login_required

@home.route("/nutricionista_home_page")
#@login_required
def nutricionista_home_page():
    return render_template("home/nutricionista_home.html")