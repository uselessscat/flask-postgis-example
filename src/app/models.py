from geoalchemy2 import Geometry

from app import db


class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trading_name = db.Column(db.String(200), nullable=False)
    owner_name = db.Column(db.String(200), nullable=False)
    document = db.Column(db.String(100), nullable=False, unique=True)
    coverage_area = db.Column(Geometry('MULTIPOLYGON'))
    address = db.Column(Geometry('POINT'))
