from geoalchemy2 import Geometry

from app import db


class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trading_name = db.Column(db.String(200), nullable=False)
    owner_name = db.Column(db.String(200), nullable=False)
    document = db.Column(db.String(100), nullable=False, unique=True)

    # geometry == cartesian, srid 4326 == WGS 84
    coverage_area = db.Column(
        Geometry(geometry_type='MULTIPOLYGON', srid=4326)
    )
    address = db.Column(Geometry(geometry_type='POINT', srid=4326))
