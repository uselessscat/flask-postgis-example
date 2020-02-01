from flask.wrappers import Response
from flask.testing import FlaskClient
from tests.conftest import client

from app.models import Partner


def test_create_error_on_empty(client: FlaskClient):
    print(type(client))
    res: Response = client.post('/partners/', json={})

    assert res.status == 422
