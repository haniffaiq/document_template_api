from datetime import datetime
from db import db

class BeritaAcaraPemeriksaanPekerjaan(db.Model):
    __tablename__ = 'berita_acara_pemeriksaan_pekerjaan'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    nilai_kontrak_angka = db.Column(db.Numeric(15, 2), nullable=True)
    nilai_kontrak_huruf = db.Column(db.String(255), nullable=True)
    nomor_addendum = db.Column(db.String(100), nullable=True)
    nilai_addendum = db.Column(db.Numeric(15, 2), nullable=True)
    tanggal_addendum = db.Column(db.Date, nullable=True)
    persentase_fisik_pekerjaan = db.Column(db.Numeric(5, 2), nullable=True)
    
    # Relasi dengan tabel Project
    project = db.relationship('Project', backref=db.backref('berita_acara_pemeriksaan_pekerjaan', cascade='all, delete-orphan'), lazy=True)
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
