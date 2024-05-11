class Config:
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USER_TLS = True
    MAIL_USERNAME = "nutriplus2024@gmail.com"
    MAIL_PASSWORD = "nutriplus123"

    SECRET_KEY = "segredo"

class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

config = {
    "develop": DevelopConfig(),
    "test": TestConfig()
}