from flask import Flask

from config import config

from .ext.db import db
from .ext.bootstrap5 import bootstrap


app = Flask(__name__)

def create_app(config_name: str):
    app.config.from_object(config[config_name])

    db.init_app(app)
    bootstrap.init_app(app)

    from .controllers.home import home as home_bluesprint
    app.register_blueprint(home_bluesprint)

    from .controllers.diet import diet as diet_bluesprint
    app.register_blueprint(diet_bluesprint)

    return app


