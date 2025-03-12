from datetime import datetime
from db import db

class Kwitansi(db.Model):
    __tablename__ = 'kwitansi'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    telah_diterima_dari = db.Column(db.String(255), nullable=True)
    nomor_surat_sumber_dana = db.Column(db.String(255), nullable=True)
    tanggal_surat_sumber_dana = db.Column(db.Date, nullable=True)
    uang_sebanyak = db.Column(db.Numeric, nullable=True)
    uang_sebanyak_huruf = db.Column(db.String(255), nullable=True)
    untuk_pembayaran = db.Column(db.String(255), nullable=True)
    nama_tambahan = db.Column(db.String(255), nullable=True)

    # Relasi dengan tabel Project
    project = db.relationship('Project', backref=db.backref('kwitansi', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
