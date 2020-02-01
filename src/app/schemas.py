from geoalchemy2.elements import WKBElement
from geoalchemy2.shape import to_shape, from_shape
from shapely.geometry import mapping, shape as Shape

from marshmallow.fields import Field
from marshmallow_sqlalchemy import ModelSchema

from app import db
from app.models import Partner


class Geo(Field):
    def _deserialize(
            self,
            value: dict = None,
            attr=None,
            data=None,
            **kwargs) -> WKBElement:
        shape: Shape = Shape(value)

        return from_shape(shape)

    def _serialize(
            self,
            value: WKBElement = None,
            *args,
            **kwargs
    ) -> dict:
        if value is None or value == '':
            return {}

        shape: Shape = to_shape(value)

        return mapping(shape)


class PartnerSchema(ModelSchema):
    class Meta:
        model = Partner
        sqla_session = db

    address = Geo()
    coverage_area = Geo()


partner_schema = PartnerSchema()
partners_schema = PartnerSchema(many=True)
