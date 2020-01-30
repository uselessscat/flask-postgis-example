from flask import Blueprint
from app.models import Partner

partners_blueprint = Blueprint('partners', __name__, url_prefix='/partners')


@partners_blueprint.route('/<int:id>', methods=['GET'])
def get_partner(id: int) -> tuple:
    return 'get_by_id', 200


@partners_blueprint.route('/', methods=['POST'])
def create_partner() -> tuple:
    return 'create', 200
