import uuid
from datetime import datetime
from db import db


class Role(db.Model):
    __tablename__ = 'roles'
    __table_args__ = {'schema': 'authentication'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Role(id={self.id}, name='{self.name}', is_deleted={self.is_deleted})>"

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'authentication'}

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('authentication.roles.id'), nullable=False)  # Adjusted ForeignKey
    is_deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = db.Column(db.DateTime)

    role = db.relationship('Role', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}', role='{self.role.name}')>"
