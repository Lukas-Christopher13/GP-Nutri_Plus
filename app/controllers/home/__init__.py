from flask import Blueprint

home = Blueprint("home", __name__)

from . import home_controller, cliente_home, nutricionista_home

