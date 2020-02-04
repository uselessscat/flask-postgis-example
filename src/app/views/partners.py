from typing import Tuple

from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest

from sqlalchemy import asc
from shapely.geometry import Point
from geoalchemy2.functions import ST_Contains, ST_Distance
from geoalchemy2.shape import from_shape

from app import db
from app.models import Partner
from app.serializers import partner_serializer

partners_blueprint: Blueprint = Blueprint(
    'partners', __name__, url_prefix='/partners'
)


@partners_blueprint.route('/<int:id>', methods=['GET'])
def get_partner(id: int) -> Tuple[dict, int]:
    partner: Partner = Partner.query.filter_by(id=id).first()

    return partner_serializer.dump(partner), 200


@partners_blueprint.route('/', methods=['POST'])
def create_partner() -> Tuple[dict, int]:
    try:
        if not request.is_json:
            raise BadRequest

        request_data: dict = request.json

        # Avoid updating by id.
        # TODO: investigate if library allows to ignore it
        if request_data.get('id') is not None:
            del request_data['id']

        partner: Partner = partner_serializer.load(request_data)

        db.session.add(partner)
        db.session.commit()
    except BadRequest:
        return jsonify({'error': 'Content is not json'}), 422

    return partner_serializer.dump(partner), 201


@partners_blueprint.route('/search', methods=['GET'])
def search_partner() -> Tuple[dict, int]:
    lng: float = float(request.args.get('lng'))
    lat: float = float(request.args.get('lat'))

    point = from_shape(Point(lng, lat), srid=4326)

    results: Tuple[Partner, float] = Partner.query \
        .add_columns(ST_Distance(Partner.address, point).label('dist')) \
        .filter(ST_Contains(Partner.coverage_area, point)) \
        .order_by(asc('dist')) \
        .first()

    if results is None:
        return jsonify({}), 200

    return partner_serializer.dump(results[0]), 200
