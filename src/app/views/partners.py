from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest

from app import db
from app.models import Partner
from app.serializers import partner_serializer

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

    # TODO: try https://stackoverflow.com/a/56515229/6658955
    return partner_serializer.dump(partner), 201


@partners_blueprint.route('/search', methods=['GET'])
def search_partner() -> tuple:
    return 'search', 200
