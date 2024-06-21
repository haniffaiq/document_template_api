# auth_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers.auth.auth_controller import register_user, login_user,update_guest_role
from middleware import check_role  # Mengimpor middleware check_role

auth_bp = Blueprint('auth', __name__)

# Contoh endpoint yang memerlukan otorisasi sebagai SUPERADMIN
@auth_bp.route('/update_role', methods=['POST'])
@jwt_required()
@check_role('SUPERADMIN')  # Menggunakan middleware check_role
def update_role():
    data = request.get_json()
    result = update_guest_role(data)
    return result

# Endpoint untuk register user
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result = register_user(data)
    return result

# Endpoint untuk login user
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result = login_user(data)
    return result
