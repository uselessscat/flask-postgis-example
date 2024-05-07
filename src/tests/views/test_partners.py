from flask import Flask
from flask.wrappers import Response
from flask.testing import FlaskClient

from tests.sample_data import partners as partner_samples

from app import db
from app.models import Partner


def test_create_error_on_empty(client: FlaskClient) -> None:
    res: Response = client.post('/partners/', json={})

    assert res.content_type == 'application/json'

    # because of required data
    assert res.status_code == 400

    assert res.json['error']['code'] == 400
    assert res.json['error']['message'] == 'Validation error'


def test_create_valid_data(app: Flask, client: FlaskClient) -> None:
    sample: dict = partner_samples.get_camel()

    res: Response = client.post('/partners/', json=sample)

    json_res: dict = res.json

    assert res.content_type == 'application/json'
    assert res.status_code == 201

    assert json_res.get('id') == 1
    assert json_res == sample

    with app.app_context():
        assert db.session.get(Partner, 1) is not None


def test_search_closest(app: Flask, client: FlaskClient) -> None:
    # Create partner
    sample: dict = partner_samples.get_camel()
    client.post('/partners/', json=sample)

    res: Response = client.get(
        '/partners/search',
        query_string={'lat': 0.15, 'lng': 0.15}
    )

    json_res: dict = res.json

    assert res.content_type == 'application/json'
    assert res.status_code == 200

    assert json_res == sample


def test_search_closest_no_match(app: Flask, client: FlaskClient) -> None:
    # Create partner
    sample: dict = partner_samples.get_camel()
    client.post('/partners/', json=sample)

    res: Response = client.get(
        '/partners/search',
        query_string={'lat': -1, 'lng': -1}
    )

    json_res: dict = res.json

    assert res.content_type == 'application/json'
    assert res.status_code == 200

    assert json_res == {}


def test_search_closest_match_between(app: Flask, client: FlaskClient) -> None:
    # Create partner 1
    sample_1: dict = partner_samples.get_camel()
    sample_1['address']['coordinates'] = [0.25, 0.25]

    # Create partner 2
    sample_2: dict = partner_samples.get_camel()
    sample_2['document'] = '123456789/5678'
    sample_2['address']['coordinates'] = [0.01, 0.01]

    # check that is no same object
    assert sample_1 != sample_2

    res_1: Response = client.post('/partners/', json=sample_1)
    res_2: Response = client.post('/partners/', json=sample_2)

    assert res_1.status_code == 201
    assert res_2.status_code == 201
    assert res_1.json != res_2.json

    with app.app_context():
        assert Partner.query.count() == 2

    res: Response = client.get(
        '/partners/search',
        query_string={'lat': 0.45, 'lng': 0.45}
    )
    json_res: dict = res.json

    assert res.content_type == 'application/json'
    assert res.status_code == 200

    # must match sample_1 because it's closer
    assert json_res == sample_1
    assert json_res != sample_2
