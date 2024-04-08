from flask import Blueprint

diet = Blueprint("diet", __name__)

from . import diet_controller