import logging

from datetime import datetime

from . import notification

from ...ext.db import db
from ...models.nuticionista_model import Notification

from ...utils.log import my_log

NUTRICIONISTA_TEST = "1dcb552e-a945-466c-8c52-e62a976ce89a"

@notification.route("/send_notification_test")
def send_notification_test():
    start_time = datetime.now().strftime('%H:%M:%S')

    send_notification()

    end_time = datetime.now().strftime('%H:%M:%S')

    my_log.info(f"START TIME: {start_time} | END TIME: {end_time}")

    return f"notificação enviada: start: {start_time} | end: {end_time}"

def send_notification( ):
    message = f"TEST | TIME: '{datetime.now().strftime('%H:%M:%S')}' | M: mensagem de teste"
    nutricionista = NUTRICIONISTA_TEST
 
    notification = Notification(message=message, nutricionista_id=nutricionista)

    db.session.add(notification)
    db.session.commit()

