class Config:
    SECRET_KEY = "segredo"
    JWT_SECRET_KEY = "super-secret"

class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

config = {
    "develop": DevelopConfig(),
    "test": TestConfig()
}