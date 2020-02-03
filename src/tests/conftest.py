import os
import pytest

from app import create_app, db


@pytest.fixture
def app() -> None:
    os.environ['APP_SETTINGS'] = 'app.configs.TestingConfig'

    app = create_app()

    with app.app_context():
        # TODO: create test database with geographic modules
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app) -> None:
    return app.test_client()
