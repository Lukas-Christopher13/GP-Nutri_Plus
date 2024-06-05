from flask import Blueprint

diet = Blueprint("diet", __name__, url_prefix='/diet')

from . import diet_controller