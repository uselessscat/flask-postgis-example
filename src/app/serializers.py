from typing import Optional

from geoalchemy2.elements import WKBElement
from geoalchemy2.shape import to_shape, from_shape
from shapely.geometry import mapping, shape as Shape

from marshmallow.fields import Field
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from app import db
from app.utils import camelcase
from app.models import Partner


class GeometryField(Field):
    def _deserialize(
        self,
        value: Optional[dict] = None,
        *args,
        **kwargs,
    ) -> WKBElement:
        shape: Shape = Shape(value)

        return from_shape(shape, srid=4326)

    def _serialize(
        self,
        value: Optional[WKBElement] = None,
        *args,
        **kwargs,
    ) -> dict:
        if value is None or value == '':
            return {}

        shape: Shape = to_shape(value)

        return mapping(shape)


class PartnerSerializer(SQLAlchemySchema):
    class Meta:
        model = Partner
        load_instance = True
        sqla_session = db.session

    id = auto_field()
    trading_name = auto_field()
    owner_name = auto_field()
    document = auto_field()
    address = GeometryField()
    coverage_area = GeometryField()

    def on_bind_field(self, field_name: str, field_obj: Field) -> None:
        field_obj.data_key = camelcase(field_obj.data_key or field_name)


partner_serializer = PartnerSerializer()
partners_serializer = PartnerSerializer(many=True)
