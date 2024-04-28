from flask import Blueprint

activity = Blueprint("activity", __name__, url_prefix='/activity')

from . import activity_controller