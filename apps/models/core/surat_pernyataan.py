from datetime import datetime
from db import db

class SuratPernyataan(db.Model):
    __tablename__ = 'surat_pernyataan'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    nomor_surat = db.Column(db.String(255), nullable=True)
    perihal_surat = db.Column(db.String(255), nullable=True)
    perihal_keterangan = db.Column(db.Text, nullable=True)
    tahun_anggaran = db.Column(db.Integer, nullable=True)
    nilai_kontrak_angka = db.Column(db.Numeric, nullable=True)
    nilai_kontrak_huruf = db.Column(db.String(255), nullable=True)
    nomor_surat_keputusan_rektor = db.Column(db.String(255), nullable=True)
    tanggal_surat_keputusan_rektor = db.Column(db.Date, nullable=True)

    # Relasi
    project = db.relationship('Project', backref=db.backref('surat_pernyataan', cascade='all, delete-orphan'), lazy=True)
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        result = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        if self.tanggal_surat_keputusan_rektor:
            result['tanggal_surat_keputusan_rektor'] = self.tanggal_surat_keputusan_rektor.strftime('%d-%m-%Y')
        return result
