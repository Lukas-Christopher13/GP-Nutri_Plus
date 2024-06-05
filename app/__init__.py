from flask import Flask, request, g

from config import config

from .ext.db import db
from .ext.mail import mail
from .ext.bootstrap5 import bootstrap
from .ext.flask_login import login_manager
from .services.lembrete_consulta_service import init_scheduler

import time
import logging


app = Flask(__name__)

def create_app(config_name: str):
    app.config.from_object(config[config_name])

    db.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    from .controllers.home import home as home_bluesprint
    app.register_blueprint(home_bluesprint)

    from .controllers.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .controllers.diet import diet as diet_bluesprint
    app.register_blueprint(diet_bluesprint)

    from .controllers.exam import exam as exam_bluesprint
    app.register_blueprint(exam_bluesprint)

    from .controllers.cliente import cliente as cliente_blueprint
    app.register_blueprint(cliente_blueprint, url_prefix="/cliente")

    from .controllers.nutricionista import nutricionista as nutricionista_blueprint
    app.register_blueprint(nutricionista_blueprint, url_prefix="/nutricionista")

    from .controllers.activity import activity as activity_blueprint
    app.register_blueprint(activity_blueprint)

    from .controllers.notification import notification as notification_blueprint
    app.register_blueprint(notification_blueprint)

    init_scheduler(app)

    #tempo de resposta com middleware
    @app.before_request
    def start_timer():
        g.start_time = time.time()

    @app.after_request
    def log_response_time(response):
        if hasattr(g, 'start_time'):
            response_time = time.time() - g.start_time
            app.logger.info(f"Request to {request.path} took {response_time:.4f} seconds")
        return response

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    
    app.logger.propagate = False

    return app


