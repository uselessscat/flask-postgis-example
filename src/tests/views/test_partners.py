from flask.wrappers import Response
from flask.testing import FlaskClient

from tests.sample_data import partners as partner_samples


def test_create_error_on_empty(client: FlaskClient):
    res: Response = client.post('/partners/', json={})

    assert res.content_type == 'application/json'

    # because of required data
    assert res.status_code == 400

    assert res.json['error']['code'] == 400
    assert res.json['error']['message'] == 'Validation error'


def test_create_valid_data(client: FlaskClient):
    sample: dict = partner_samples.get_camel()

    res: Response = client.post('/partners/', json=sample)

    json_res: dict = res.json

    assert res.content_type == 'application/json'
    assert res.status_code == 201

    assert json_res.get('id') == 1
    assert json_res == sample
