from flask import Flask, jsonify

from marshmallow.exceptions import ValidationError


def build_error(code: int, message: str = '', details: list = []) -> dict:
    return {
        'error': {
            'code': code,
            'message': message,
            'details': details
        }
    }


def register_exception_handlers(app: Flask) -> None:
    @app.errorhandler(ValidationError)
    def validation_exception(e: ValidationError) -> tuple:
        return jsonify(build_error(
            code=400,
            message='Validation error',
            # TODO: generate better details
            details=e.normalized_messages()
        )), 400
