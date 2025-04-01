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

    # Kolom yang dihapus
    # nama_tambahan = db.Column(db.String(255), nullable=True)  # Dihapus

    # Kolom yang ditambahkan
    surat_addendum = db.Column(db.String(255), nullable=True)  # Surat Addendum
    tanggal_surat_addendum = db.Column(db.Date, nullable=True)  # Tanggal Surat Addendum

    # Relasi dengan tabel Project
    project = db.relationship('Project', backref=db.backref('kwitansi', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        result = {column.name: getattr(self, column.name) for column in self.__table__.columns}

        # Format tanggal menjadi DD-MM-YYYY jika ada
        if self.tanggal_surat_sumber_dana:
            result['tanggal_surat_sumber_dana'] = self.tanggal_surat_sumber_dana.strftime('%d-%m-%Y')
        if self.tanggal_surat_addendum:
            result['tanggal_surat_addendum'] = self.tanggal_surat_addendum.strftime('%d-%m-%Y')

        return result
