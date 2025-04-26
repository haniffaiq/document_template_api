from datetime import datetime
from db import db

class BeritaAcaraSerahTerimaUangMuka(db.Model):
    __tablename__ = 'berita_acara_serah_terima_uang_muka'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    nomor_berita_acara_serah_terima_uang_muka = db.Column(db.String(255), nullable=True)
    tanggal_berita_acara_serah_terima_uang_muka = db.Column(db.Date, nullable=True)
    tanggal_berita_acara_serah_terima_uang_muka_huruf = db.Column(db.String(255), nullable=True)
    nilai_kontrak = db.Column(db.Numeric, nullable=True)
    tanggal_surat_perjanjian_kontrak = db.Column(db.Date, nullable=True)
    jumlah_yang_dibulatkan_total = db.Column(db.Numeric, nullable=True)
    jumlah_yang_dibulatkan_huruf = db.Column(db.String(255), nullable=True)
    untuk_bulan = db.Column(db.Text, nullable=True)


    # Relasi dengan tabel Project
    project = db.relationship('Project', backref=db.backref('berita_acara_serah_terima_uang_muka', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
