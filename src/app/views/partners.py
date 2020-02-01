from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest

from app import db
from app.models import Partner
from app.schemas import partner_schema

partners_blueprint = Blueprint('partners', __name__, url_prefix='/partners')


@partners_blueprint.route('/<int:id>', methods=['GET'])
def get_partner(id: int) -> tuple:
    return 'get_by_id', 200


@partners_blueprint.route('/', methods=['POST'])
def create_partner() -> tuple:
    try:
        if not request.is_json:
            raise BadRequest

        request_data: dict = request.json
        partner: Partner = partner_schema.load(request_data)

        db.session.add(partner)
        db.session.commit()
    except BadRequest:
        return jsonify({'error': 'Content is not json'}), 422

    # TODO: try https://stackoverflow.com/a/56515229/6658955
    return partner_schema.dump(partner), 201
