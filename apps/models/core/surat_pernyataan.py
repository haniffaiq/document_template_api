from datetime import datetime
from db import db

class SuratPernyataan(db.Model):
    __tablename__ = 'surat_pernyataan'
    __table_args__ = {'schema': 'ikram'}
    
    # Kolom yang ada sebelumnya
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    nomor_surat = db.Column(db.String(255), nullable=True)  # Kolom nomor_surat dikembalikan
    perihal_surat = db.Column(db.String(255), nullable=True)
    perihal_keterangan = db.Column(db.Text, nullable=True)
    tahun_anggaran = db.Column(db.Integer, nullable=True)
    nilai_kontrak_angka = db.Column(db.Numeric, nullable=True)
    nilai_kontrak_huruf = db.Column(db.String(255), nullable=True)
    
    # Kolom baru
    hari_dan_tanggal_surat_pernyataan_angka = db.Column(db.Date, nullable=True)  # Tanggal dalam format dd/mm/yyyy
    nomor_surat_keputusan_rektor = db.Column(db.String(255), nullable=True)  # Nomor surat keputusan rektor
    tanggal_surat_keputusan_rektor = db.Column(db.Date, nullable=True)  # Tanggal keputusan rektor

    # Relasi dengan tabel Project
    project = db.relationship('Project', backref=db.backref('surat_pernyataan', cascade='all, delete-orphan'), lazy=True)
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        # Mengembalikan semua kolom ke dalam dictionary
        result = {column.name: getattr(self, column.name) for column in self.__table__.columns}

        # Format tanggal ke DD-MM-YYYY jika ada nilai tanggal
        if self.hari_dan_tanggal_surat_pernyataan_angka:
            result['hari_dan_tanggal_surat_pernyataan_angka'] = self.hari_dan_tanggal_surat_pernyataan_angka.strftime('%d-%m-%Y')
        if self.tanggal_surat_keputusan_rektor:
            result['tanggal_surat_keputusan_rektor'] = self.tanggal_surat_keputusan_rektor.strftime('%d-%m-%Y')

        return result
