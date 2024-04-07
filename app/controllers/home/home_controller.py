from . import home

from flask import render_template

@home.route("/")
def home():
    return render_template("home/index.html")