from flask import Flask, request
from user_agents import parse

app = Flask(__name__)

@app.route('/')
def index():

    client_ip = request.remote_addr
    user_agent_string = request.headers.get('User-Agent')
    user_agent = parse(user_agent_string)

    os = user_agent.os.family  
    device = user_agent.device.family 
    browser = user_agent.browser.family 

    if user_agent.is_mobile:
        device_type = 'Mobile'
    elif user_agent.is_tablet:
        device_type = 'Tablet'
    elif user_agent.is_pc:
        device_type = 'PC'
    else:
        device_type = 'Desconhecido'

    response = (
        f"IP do cliente: {client_ip}<br>"
        f"Sistema Operacional: {os}<br>"
        f"Nome do Dispositivo: {device}<br>"
        f"Navegador: {browser}<br>"
        f"Tipo de Dispositivo: {device_type}<br>"
        f"User-Agent: {user_agent_string}<br>"
    )

    return response

if __name__ == '__main__':
    app.run(debug=True)
