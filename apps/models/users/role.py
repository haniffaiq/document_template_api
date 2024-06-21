from db import db

class Role(db.Model):
    __tablename__ = 'roles'
    __table_args__ = {'schema': 'authentication'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Role(id={self.id}, name='{self.name}', is_deleted={self.is_deleted})>"
