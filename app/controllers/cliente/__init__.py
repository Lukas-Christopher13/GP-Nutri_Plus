from flask import Blueprint

cliente = Blueprint("cliente", __name__)

from . import agendar_consulta