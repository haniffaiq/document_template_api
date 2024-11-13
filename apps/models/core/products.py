import uuid
from datetime import datetime
from db import db

# Model untuk Produk
class Product(db.Model):
    __tablename__ = 'products'
    __table_args__ = {'schema': 'core'}

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))  # UUID sebagai string
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    stock_quantity = db.Column(db.Integer, default=0)
    is_deleted = db.Column(db.Integer, default=0)  # Status penghapusan (0 = aktif, 1 = dihapus)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, stock_quantity={self.stock_quantity})>"

# Model untuk Pergerakan Stok
class StockMovement(db.Model):
    __tablename__ = 'stock_movements'
    __table_args__ = {'schema': 'core'}

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))  # UUID sebagai string
    product_id = db.Column(db.String(36), db.ForeignKey('inventory.products.id'), nullable=False)
    movement_type = db.Column(db.String(50), nullable=False)  # 'in' untuk barang masuk, 'out' untuk barang keluar
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.DECIMAL(10, 2), nullable=False)
    movement_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    is_deleted = db.Column(db.Integer, default=0)  # Status penghapusan (0 = aktif, 1 = dihapus)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)

    product = db.relationship("Product", backref=db.backref('movements', lazy=True))

    def __repr__(self):
        return f"<StockMovement(id={self.id}, product_id='{self.product_id}', movement_type='{self.movement_type}', quantity={self.quantity})>"
