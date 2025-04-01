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
    nominal_termin = db.Column(db.Numeric, nullable=True)
    jumlah_yang_dibulatkan_huruf = db.Column(db.String(255), nullable=True)
    
    # Kolom baru yang ditambahkan
    termin = db.Column(db.Integer, nullable=True)  # Kolom untuk nomor termin
    total_uang_progress_fisik = db.Column(db.Numeric, nullable=True)  # Kolom untuk total uang progres fisik
    jumlah_yang_sudah_dibayar = db.Column(db.Numeric, nullable=True)  # Kolom untuk jumlah yang sudah dibayar
    tahap_terbilang = db.Column(db.String(255), nullable=True)  # Kolom untuk tahap terbilang
    
    # Relasi dengan tabel Project
    project = db.relationship('Project', backref=db.backref('berita_acara_pembayaran_termin', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        # Membuat dictionary dari kolom-kolom model untuk API response
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
