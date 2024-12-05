from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models import User
from src.schemas import UserSchema
from src.extensions import db
from src.decorators import admin_required

users = Blueprint('users', __name__)


@users.route('/me', methods=['GET'])
@jwt_required()
def get_profile():
    current_user = get_jwt_identity()

    return jsonify(current_user), 200


@users.route('/', methods=['GET'])
@jwt_required()
@admin_required
def list_users():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    users = User.query.paginate(page=page, per_page=per_page)
    user_schema = UserSchema(many=True)

    return jsonify({
        "users": user_schema.dump(users.items),
        "total": users.total,
        "page": users.page,
        "per_page": users.per_page
    }), 200


@users.route('/', methods=['POST'])
@jwt_required()
@admin_required
def create_user():
    user_schema = UserSchema(many=True)
    # Validate the input data
    data = user_schema.load(request.json, partial=True)  # Allow partial updates

    user = User(
        username=data['username'],
        email=data['email'],
        role=data.get('role', 'user'),
        is_active=True
    )
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return user_schema.dump(user), 201


@users.route('/<int:id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_user():
    user = User.query.get_or_404(id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    user_schema = UserSchema(many=True)
    # Validate the input data
    data = user_schema.load(request.json, partial=True)  # Allow partial updates

    # Update the product's fields with validated data
    if "username" in data:
        user.username = data["username"]
    if "email" in data:
        user.email = data["email"]
    if "role" in data:
        user.role = data["role"]
    if "is_active" in data:
        user.is_active = data["is_active"]

    if "password" in data:
        user.set_password(data['password'])

    # Commit the changes to the database
    db.session.commit()

    # Return the updated product
    return user_schema.dump(user), 200
