# auth_controller.py

from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from models.users.users import User, Role 
from db import db
import hashlib
from middleware import check_role, get_jwt_identity
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity

# Fungsi-fungsi utilitas
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def check_password_hash(stored_password, provided_password):
    hashed_provided_password = hashlib.sha256(provided_password.encode()).hexdigest()
    return hashed_provided_password == stored_password

def generate_token(username, role):
    access_token = create_access_token(identity=username, additional_claims={"role": role})
    return access_token

def register_user(data):
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role_name = 'GUEST'  # Role default untuk user baru

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"}), 400

    hashed_password = hash_password(password)
    role = Role.query.filter_by(name=role_name).first()  # Pastikan Role telah diimport dari model
    if not role:
        return jsonify({"message": f"Role {role_name} not found"}), 404

    new_user = User(username=username, password=hashed_password, email=email, role_id=role.id)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

def update_guest_role(data):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"message": "Authorization header is missing"}), 401

    try:
        guest_username = data.get('username')
        new_role_name = data.get('role')

        guest_user = User.query.filter_by(username=guest_username).first()
        if not guest_user or guest_user.role.name == 'SUPERADMIN':
            return jsonify({"message": "Guest user not found or cannot be updated"}), 404

        new_role = Role.query.filter_by(name=new_role_name).first()
        if not new_role:
            return jsonify({"message": f"Role {new_role_name} not found"}), 404

        guest_user.role_id = new_role.id
        db.session.commit()

        return jsonify({"message": f"Role of {guest_username} updated successfully"}), 200

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

def login_user(data):
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        role = user.role.name  # Ambil role dari objek user
        token = generate_token(username, role)  # Generate token dengan role
        return jsonify({
            "status": 200,
            "message": "Login successful",
            "data": {"token": token}
        }), 200
    else:
        return jsonify({
            "status": 401,
            "message": "Invalid Credential"
        }), 401
