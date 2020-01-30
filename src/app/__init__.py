import os

from flask import Flask


def register_blueprints(app: Flask) -> None:
    from app.views.meta import meta_blueprint
    from app.views.partners import partners_blueprint

    app.register_blueprint(meta_blueprint)
    app.register_blueprint(partners_blueprint)


def create_app() -> Flask:
    app = Flask(__name__)

    register_blueprints(app)

    return app
