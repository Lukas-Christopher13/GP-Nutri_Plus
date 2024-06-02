from flask_mail import Message

from ...ext.db import db

from ...ext.mail import mail
from ...models.cliente_model import Cliente
from ...models.nuticionista_model import Notification
from ...utils.log import my_log

def notificar(cliente: Cliente, message):
    nutricionista = cliente.nutricionista_id
 
    notification = Notification(message=message, nutricionista_id=nutricionista)

    db.session.add(notification)
    db.session.commit()

    my_log.info("Notificação Enviada!")

    if verify_if_notification_is_sendend(notification):
        db.session.add(notification)
        db.session.commit()

        my_log.info("A notificação teve que ser reenviada!")
        
def verify_if_notification_is_sendend(notification: Notification):
    notification = Notification.query.filter_by(id = notification.id).first()

    if notification is None:
        return True
    return False
