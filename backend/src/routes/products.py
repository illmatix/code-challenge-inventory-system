from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from src.models import Product
from src.extensions import db
from src.schemas import ProductSchema
from src.decorators import admin_required
from datetime import datetime

products = Blueprint('products', __name__)


@products.route('/', methods=['GET'])
def list_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    products = Product.query.filter_by(deleted_at=None).paginate(page=page, per_page=per_page)
    product_schema = ProductSchema(many=True)

    return jsonify(product_schema.dump(products)), 200


@products.route('/', methods=['POST'])
@jwt_required()
@admin_required
def create_product():
    data = request.get_json()
    product_schema = ProductSchema()
    product = product_schema.load(data)

    db.session.add(product)
    db.session.commit()
    return product_schema.dump(product), 201


@products.route('/<int:id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product_schema = ProductSchema()

    updated_product = product_schema.load(data, instance=product, partial=True)
    db.session.commit()
    return product_schema.dump(updated_product), 200


@products.route('/<int:id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_product(id):
    product = Product.query.get_or_404(id)
    product.deleted_at = datetime.utcnow()
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 200
