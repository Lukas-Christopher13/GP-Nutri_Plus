import logging
import time

from datetime import datetime

from . import notification

from ...ext.db import db
from ...models.nuticionista_model import Notification

from ...utils.log import my_log

NUTRICIONISTA_TEST = "fc33f22f-4280-437c-880c-20310908f968"

@notification.route("/send_notification_test")
def send_notification_test():
    start_time = time.time()

    send_notification()

    end_time = time.time()

    my_log.info(f"START TIME: {start_time} | END TIME: {end_time} | Result {end_time - start_time}")

    return f"notificação enviada: start: {start_time} | end: {end_time}"

def send_notification( ):
    message = f"TEST | TIME: '{datetime.now().strftime('%H:%M:%S')}' | M: mensagem de teste"
    nutricionista = NUTRICIONISTA_TEST
 
    notification = Notification(message=message, nutricionista_id=nutricionista)

    db.session.add(notification)
    db.session.commit()

