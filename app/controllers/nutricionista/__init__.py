from flask import Blueprint

nutricionista = Blueprint("nutricionista", __name__)

from . import calendario, monitorar_paciente