from datetime import datetime
from db import db

class BeritaAcaraPembayaranTermin(db.Model):
    __tablename__ = 'berita_acara_pembayaran_termin'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    nama_termin_ke = db.Column(db.String(255), nullable=True)
    persentase_pekerjaan = db.Column(db.Numeric, nullable=True)
    jumlah_persentase_uang_muka = db.Column(db.Numeric, nullable=True)
    jumlah_uang_muka = db.Column(db.Numeric, nullable=True)
    total_uang_muka = db.Column(db.Numeric, nullable=True)
    jumlah_persentase_uang_progres_fisik = db.Column(db.Numeric, nullable=True)
    jumlah_uang_progres_fisik = db.Column(db.Numeric, nullable=True)
    jumlah_persentase_retensi_pekerjaan = db.Column(db.Numeric, nullable=True)
    jumlah_uang_retensi_pekerjaan = db.Column(db.Numeric, nullable=True)
    jumlah_persentase_pengembalian_uang_muka = db.Column(db.Numeric, nullable=True)
    jumlah_pengembalian_uang_muka = db.Column(db.Numeric, nullable=True)
    jumlah_yang_harus_dibayar = db.Column(db.Numeric, nullable=True)
    jumlah_yang_dibulatkan = db.Column(db.Numeric, nullable=True)
    jumlah_yang_dibulatkan_huruf = db.Column(db.String(255), nullable=True)

    # Relasi dengan tabel Project
    project = db.relationship('Project', backref=db.backref('berita_acara_pembayaran_termin', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
