from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.users.users import User
from db import db
import hashlib
from flask_jwt_extended import JWTManager, create_access_token

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def check_password_hash(stored_password, provided_password):
    hashed_provided_password = hashlib.sha256(provided_password.encode()).hexdigest()
    return hashed_provided_password == stored_password
def generate_token(username):
    return create_access_token(identity=username)



def register_user(data):
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"}), 400

    hashed_password = hash_password(password)
    new_user = User(username=username, password=hashed_password, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

def login_user(data):
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        token = generate_token(username)        
        return jsonify({"status": 200,
                        "message": "Login successful",
                        "data": 
                            {"token" : token}}), 200
    else:
        return jsonify({"status": 401,
                        "message": "Invalid Credential",}), 401
