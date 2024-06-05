from flask import Flask
from flask_jwt_extended import JWTManager
from db import db
from routes import register_routes
from dotenv import load_dotenv
import os


def create_app():
    app = Flask(__name__)
    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    db.init_app(app)

    with app.app_context():
        from db import test_db_connection
        if test_db_connection():
            print("Database connection successful!")
        else:
            print("Failed to connect to the database.")

    register_routes(app)
    jwt = JWTManager(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
