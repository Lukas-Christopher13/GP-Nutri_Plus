import uuid

from sqlalchemy import Column, String, ForeignKey

from user_agents import parse

from ..ext.db import db

class Dispositivo(db.Model):
    __tablename__ = "dispositivo"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nutricionista_id = Column(String(36), ForeignKey("nutricionista.id"), nullable=False)
    ip = Column(String())
    os = Column(String())
    device = Column(String())
    device_type = Column(String())
    browser_type = Column(String())
    user_agent = Column(String())

    @staticmethod
    def register_divice(request, nutricionista):
        dispositivo = Dispositivo.create_divice(request, nutricionista)

        db.session.add(dispositivo)
        db.session.commit()

    @staticmethod
    def create_divice(request, nutricionista):
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
    
        dispositivo = Dispositivo(
            nutricionista_id = nutricionista.id,
            ip=client_ip,
            os=os,
            browser_type=browser,
            device=device,
            device_type=device_type,
            user_agent=user_agent_string
        )

        return dispositivo

    def __eq__(self,  other: object) -> bool:
        return self.ip == other.ip and \
               self.os == other.os and \
               self.device == other.device and \
               self.device_type == other.device_type and \
               self.browser_type == other.browser_type and \
               self.user_agent == other.user_agent 
        

        


    