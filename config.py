import os
from dotenv import load_dotenv

load_dotenv("variaveis.env")

class Config:
    SECRET_KEY = "segredo"
    """MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'arthurpssilva73@gmail.com'
    MAIL_PASSWORD = ''"""
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
    CLIENT_PHONE_NUMBER = os.getenv('CLIENT_PHONE_NUMBER')



class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

config = {
    "develop": DevelopConfig(),
    "test": TestConfig()
}