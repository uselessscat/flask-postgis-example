from flask.wrappers import Response
from flask.testing import FlaskClient


def test_create_error_on_empty(client: FlaskClient):
    res: Response = client.post('/partners/', json={})

    assert res.content_type == 'application/json'

    # because of required data
    assert res.status_code == 400

    assert res.json['error']['code'] == 400
    assert res.json['error']['message'] == 'Validation error'
