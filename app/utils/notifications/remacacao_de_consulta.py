from flask_mail import Message

from ...ext.mail import mail


def notificar_remaracacao_de_consulta(sender, clinete_email):
    body_message = f"O clinete: {clinete_email}. Deseja remarcar a data de sua consulta!"
    try_send_message(sender, clinete_email, body_message)

def try_send_message(sender, cliente_email, body_message):
    try:
        send_message(sender, cliente_email, body_message)
    except:
        pass

def send_message(sender, cliente_email ,body_message):
    msg = Message("Nutri Pluas Alerta!", recipients=[cliente_email], sender=sender)
    msg.body = body_message
    mail.send(msg)
