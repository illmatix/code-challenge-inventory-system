from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError


def register_error_handlers(app):
    """
    Registers global error handlers for the application.
    """
    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return jsonify({"error": "ValidationError", "message": err.messages}), 400

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(err):
        return jsonify({"error": "IntegrityError", "message": str(err)}), 409

    @app.errorhandler(Exception)
    def handle_generic_error(err):
        return jsonify({"error": "InternalServerError", "message": str(err)}), 500
