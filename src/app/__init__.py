import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

# global db object
db = SQLAlchemy()
ma = Marshmallow()


def register_blueprints(app: Flask) -> None:
    from app.views.meta import meta_blueprint
    app.register_blueprint(meta_blueprint)

    from app.views.partners import partners_blueprint
    app.register_blueprint(partners_blueprint)


def configure_app(app: Flask) -> None:
    if(os.getenv('APP_SETTINGS') is not None):
        app.config.from_object(os.getenv('APP_SETTINGS'))
    else:
        from app.configs import DefaultConfig

        app.config.from_object(DefaultConfig)


def create_app() -> Flask:
    app: Flask = Flask(__name__)

    configure_app(app)

    # bind the libraries objects to app
    db.init_app(app)
    ma.init_app(app)

    # initialize migration library
    Migrate(app, db)

    register_blueprints(app)

    return app
