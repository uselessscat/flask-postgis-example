from typing import Tuple

from flask import Blueprint, jsonify

meta_blueprint: Blueprint = Blueprint('meta', __name__)


@meta_blueprint.route('/status', methods=['GET'])
def status() -> Tuple[dict, int]:
    return jsonify({'status': 'The server is running'}), 200
