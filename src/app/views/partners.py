from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest

from shapely.geometry import Point
from geoalchemy2.functions import ST_Contains
from sqlalchemy import func

from geoalchemy2.shape import from_shape

from app import db
from app.models import Partner
from app.serializers import partner_serializer, partners_serializer

partners_blueprint = Blueprint('partners', __name__, url_prefix='/partners')


@partners_blueprint.route('/<int:id>', methods=['GET'])
def get_partner(id: int) -> tuple:
    partner: Partner = Partner.query.filter_by(id=id).first()

    return partner_serializer.dump(partner), 200


@partners_blueprint.route('/', methods=['POST'])
def create_partner() -> tuple:
    try:
        if not request.is_json:
            raise BadRequest

        request_data: dict = request.json
        partner: Partner = partner_serializer.load(request_data)

        db.session.add(partner)
        db.session.commit()
    except BadRequest:
        return jsonify({'error': 'Content is not json'}), 422

    return partner_serializer.dump(partner), 201


@partners_blueprint.route('/search', methods=['GET'])
def search_partner() -> tuple:
    lng: str = float(request.args.get('lng'))
    lat: str = float(request.args.get('lat'))

    # st_contains(coverage_area, ST_GeometryFromText('POINT(-46.6435804 -23.5545381)', 4326))
    results = Partner.query.filter(
        func.ST_Contains(Partner.coverage_area, from_shape(Point(lng, lat), srid=4326))
    ).all()

    return jsonify(partners_serializer.dump(results)), 200
