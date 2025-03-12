from flask import Blueprint, Flask
from routers.auth.auth_routes import auth_bp 
from routers.core.products_routes import product_bp 
from routers.core.project_routes import project_bp
from routers.core.dynamic_routes import crud_bp

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(product_bp, url_prefix='/product')
    app.register_blueprint(project_bp, url_prefix='/projects')
    app.register_blueprint(crud_bp, url_prefix='/dynamic')

