from datetime import datetime
from db import db

class HistoryCrud(db.Model):
    __tablename__ = 'history_crud'
    __table_args__ = {'schema': 'ikram'}
    
    # Kolom untuk menyimpan ID unik dari history record
    id = db.Column(db.Integer, primary_key=True)
    
    # Nama tabel yang terkait dengan perubahan (misalnya 'project', 'berita_acara')
    table_name = db.Column(db.String(255), nullable=False)
    
    # ID dari record yang diubah
    record_id = db.Column(db.Integer, nullable=False)
    
    # Jenis aksi CRUD yang dilakukan ('CREATE', 'READ', 'UPDATE', 'DELETE')
    action_type = db.Column(db.String(10), nullable=False)

    
    # Timestamp perubahan
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    # ID proyek terkait (jika ada)
    project_id = db.Column(db.Integer, nullable=True)
    
    # Nama proyek terkait (jika ada)
    project_name = db.Column(db.String(255), nullable=True)
    
    # Deskripsi perubahan (opsional, untuk memberi penjelasan lebih lanjut)
    description = db.Column(db.Text, nullable=True)
    
    def __init__(self, **kwargs):
        # Inisialisasi semua kolom dengan kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def as_dict(self):
        # Mengembalikan dictionary dari objek untuk API response
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

