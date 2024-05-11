from flask import Blueprint

auth = Blueprint("auth", __name__)

from . import register, login, logout, forgot_password
