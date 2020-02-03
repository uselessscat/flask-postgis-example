from geoalchemy2.elements import WKBElement
from geoalchemy2.shape import to_shape, from_shape
from shapely.geometry import mapping, shape as Shape

from marshmallow.fields import Field
from marshmallow_sqlalchemy import ModelSchema

from app import db
from app.utils import camelcase
from app.models import Partner


class GeometryField(Field):
    def _deserialize(
            self,
            value: dict = None,
            *args,
            **kwargs) -> WKBElement:
        shape: Shape = Shape(value)

        return from_shape(shape, srid=4326)

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


class PartnerSerializer(ModelSchema):
    class Meta:
        model = Partner
        sqla_session = db.session

    address = GeometryField()
    coverage_area = GeometryField()

    def on_bind_field(self, field_name: str, field_obj: str) -> None:
        field_obj.data_key = camelcase(field_obj.data_key or field_name)


partner_serializer = PartnerSerializer()
partners_serializer = PartnerSerializer(many=True)
