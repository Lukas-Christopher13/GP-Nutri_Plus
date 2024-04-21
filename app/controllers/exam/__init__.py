from flask import Blueprint

exam = Blueprint("exam", __name__)

from . import exam_controller