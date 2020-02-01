from flask import Flask

from app import db
from app.models import Partner
from app.serializers import partner_serializer

from tests.conftest import app


def get_partner_json() -> dict:
    return {
        'id': 1,
        'tradingName': 'Adega da Cerveja - Pinheiros',
        'ownerName': 'Zé da Silva',
        'document': '1432132123891/0001',
        'coverageArea': {
            'type': 'MultiPolygon',
            'coordinates': [[[[30, 20], [45, 40], [10, 40], [30, 20]]]]
        },
        'address': {
            'type': 'Point',
            'coordinates': [30, 20]
        }
    }


def test_empty_partners(app: Flask) -> None:
    with app.app_context():
        assert len(Partner.query.all()) == 0


def test_create_partners(app: Flask) -> None:
    with app.app_context():
        partner_raw: dict = get_partner_json()

        del partner_raw['id']

        partner = partner_serializer.load(partner_raw)

        db.session.add(partner)
        db.session.commit()

        assert len(Partner.query.all()) == 1
