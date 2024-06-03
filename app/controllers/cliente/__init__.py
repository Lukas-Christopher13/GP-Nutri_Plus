from flask import Blueprint

cliente = Blueprint("cliente", __name__)

from . import agendar_consulta
from . import cancelar_consulta
from . import remarcar_consulta
from . import historioco