from flask import Flask

from config import config

from .ext.db import db
from .ext.bootstrap5 import bootstrap
from .ext.flask_login import login_manager
from app.controllers.diet.diet_controller import diet_bp


app = Flask(__name__)

def create_app(config_name: str):
    app.config.from_object(config[config_name])

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    from .controllers.home import home as home_bluesprint
    app.register_blueprint(home_bluesprint)

    from .controllers.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .controllers.diet import diet as diet_bluesprint
    app.register_blueprint(diet_bp)

    from .controllers.exam import exam as exam_bluesprint
    app.register_blueprint(exam_bluesprint)

    from .controllers.cliente import cliente as cliente_blueprint
    app.register_blueprint(cliente_blueprint, url_prefix="/cliente")

    return app


