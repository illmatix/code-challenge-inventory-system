from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from src.models import User
from src.schemas import LoginSchema

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    login_schema = LoginSchema()
    validated_data = login_schema.load(data)  # Validation handled globally

    username = validated_data["username"]
    password = validated_data["password"]

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200
    return jsonify({"error": "Invalid credentials"}), 401


@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # Add token revocation logic if needed
    return jsonify({"message": "Successfully logged out"}), 200


@auth.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    new_access_token = create_access_token(identity=identity)
    return jsonify({"access_token": new_access_token}), 200
