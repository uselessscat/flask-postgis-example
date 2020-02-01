import os
import pytest

from app import create_app, db


@pytest.fixture
def app():
    os.environ['APP_SETTINGS'] = 'app.configs.TestingConfig'

    app = create_app()

    with app.app_context():
        # TODO: create test database with geographic modules
        db.create_all()

    yield app

    with app.app_context():
        # TODO: delete database
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
