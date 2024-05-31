from flask_mail import Message

from ...ext.db import db

from ...ext.mail import mail
from ...models.cliente_model import Cliente
from ...models.nuticionista_model import Notification

def notificar_remaracacao_de_consulta(cliente: Cliente):
    message = f"O cliente {cliente.full_name} deseja remarcar a data de sua consulta!"
    nutricionista = cliente.nutricionista_id
 
    notification = Notification(message=message, nutricionista_id=nutricionista)

    db.session.add(notification)
    db.session.commit()
