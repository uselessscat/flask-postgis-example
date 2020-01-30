import os

from flask import Flask


def register_blueprints(app: Flask) -> None:
    from app.views.meta import meta_blueprint
    from app.views.partners import partners_blueprint

    app.register_blueprint(meta_blueprint)
    app.register_blueprint(partners_blueprint)


def configure_app(app: Flask) -> None:
    if(os.getenv('APP_SETTINGS') is not None):
        app.config.from_object(os.getenv('APP_SETTINGS'))
    else:
        from app.configs import DefaultConfig

        app.config.from_object(DefaultConfig)


def create_app() -> Flask:
    app = Flask(__name__)

    configure_app(app)

    register_blueprints(app)

    return app
