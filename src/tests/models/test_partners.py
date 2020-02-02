from flask import Flask

from app import db
from app.models import Partner
from app.serializers import partner_serializer

from tests.sample_data import partners as partner_samples


def test_empty_partners(app: Flask) -> None:
    with app.app_context():
        assert len(Partner.query.all()) == 0


def test_create_partners(app: Flask) -> None:
    with app.app_context():
        partner_raw: dict = partner_samples.get_w_geoobjects()

        del partner_raw['id']

        partner = Partner(**partner_raw)

        db.session.add(partner)
        db.session.commit()

        assert len(Partner.query.all()) == 1


def test_create_partners_serializer(app: Flask) -> None:
    with app.app_context():
        partner_raw: dict = partner_samples.get_camel()

        del partner_raw['id']

        partner = partner_serializer.load(partner_raw)

        db.session.add(partner)
        db.session.commit()

        assert len(Partner.query.all()) == 1
