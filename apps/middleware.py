from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
import flask_jwt_extended

def check_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()  # Verifikasi keberadaan dan keabsahan token JWT
            roles = flask_jwt_extended.get_jwt().get("role")
            # Misalnya, periksa jika current_user langsung adalah role yang diinginkan
            if roles != required_role:
                return jsonify({'message': 'Unauthorized'}), 401

            return func(*args, **kwargs)
        return wrapper
    return decorator
