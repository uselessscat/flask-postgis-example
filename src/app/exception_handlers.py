from flask import Flask, jsonify

from marshmallow.exceptions import ValidationError


def register_exception_handlers(app: Flask) -> None:
    @app.errorhandler(ValidationError)
    def validation_exception(e: ValidationError) -> tuple:
        return jsonify({
            'error': {
                'code': 400,
                'message': 'Validation error',
                # TODO: generate better details
                'details': e.normalized_messages()
            }
        }), 400
