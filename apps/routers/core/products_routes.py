from flask import Blueprint, request, jsonify
from controllers.core.products_controller import (
    create_product, get_products, get_product_by_id,
    update_product, delete_product, create_stock_movement, monitor_stock
)

product_bp = Blueprint('products', __name__)

# Route untuk membuat produk baru
@product_bp.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    return create_product(data)

# Route untuk mendapatkan semua produk
@product_bp.route('/', methods=['GET'])
def list_products():
    return get_products()

# Route untuk mendapatkan produk berdasarkan ID
@product_bp.route('/<product_id>', methods=['GET'])
def get_product(product_id):
    return get_product_by_id(product_id)

# Route untuk memperbarui produk
@product_bp.route('/<product_id>', methods=['PUT'])
def update(product_id):
    data = request.get_json()
    return update_product(product_id, data)

# Route untuk menghapus produk secara logis
@product_bp.route('/<product_id>', methods=['DELETE'])
def delete(product_id):
    return delete_product(product_id)

# Route untuk mencatat pergerakan stok
@product_bp.route('/movement', methods=['POST'])
def create_movement():
    data = request.get_json()
    return create_stock_movement(data)

# Route untuk monitoring stok dan revenue
@product_bp.route('/monitor', methods=['GET'])
def monitor():
    return monitor_stock()
