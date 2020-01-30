from flask import Blueprint, jsonify

meta_blueprint = Blueprint('meta', __name__)


@meta_blueprint.route('/status', methods=['GET'])
def status() -> tuple:
    return jsonify({'status': 'The server is running'}), 200
