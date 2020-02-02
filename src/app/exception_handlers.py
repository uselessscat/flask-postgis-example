import flask
import marshmallow


def register_exception_handlers(app: flask.Flask):
    @app.errorhandler(marshmallow.exceptions.ValidationError)
    def validation_exception(e: Exception):
        return flask.jsonify({
            'error': {
                'code': 400,
                'message': 'Validation error',
                # TODO: generate better details
                'details': e.normalized_messages()
            }
        }), 400
