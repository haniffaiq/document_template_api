from datetime import datetime
from db import db

class BeritaAcaraPemeriksaanTahapKe(db.Model):
    __tablename__ = 'berita_acara_pemeriksaan_tahap_ke'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    nomor_berita_acara = db.Column(db.String(255), nullable=True)
    tanggal_berita_acara = db.Column(db.Date, nullable=True)
    tanggal_berita_acara_huruf = db.Column(db.String(255), nullable=True)
    nilai_kontrak_angka = db.Column(db.Numeric, nullable=True)
    nilai_kontrak_huruf = db.Column(db.String(255), nullable=True)
    
    # Array untuk jenis pekerjaan yang bisa diisi secara manual
    jenis_pekerjaan = db.Column(db.ARRAY(db.String), nullable=True)
    
    # Kolom yang ditambahkan sesuai revisi
    jumlah = db.Column(db.ARRAY(db.Integer), nullable=True)  # Array of integers for jumlah pekerjaan
    satuan_pekerjaan = db.Column(db.ARRAY(db.String), nullable=True)  # Array of strings for satuan pekerjaan
    keterangan = db.Column(db.ARRAY(db.String), nullable=True)  # Array of strings for keterangan pekerjaan
    tahap = db.Column(db.String(255), nullable=True)
    tahap_terbilang = db.Column(db.String(255), nullable=True)
    nomor_surat_dipa = db.Column(db.String(255), nullable=True)
    tanggal_surat_dipa = db.Column(db.Date, nullable=True)
    nilai_pembayaran_angka = db.Column(db.Numeric, nullable=True)
    nilai_pembayaran_huruf = db.Column(db.String(255), nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relasi dengan tabel Project
    project = db.relationship('Project', backref=db.backref('berita_acara_pemeriksaan_tahap_ke', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        result = {column.name: getattr(self, column.name) for column in self.__table__.columns}

        # Format tanggal menjadi DD-MM-YYYY jika ada
        if self.tanggal_berita_acara:
            result['tanggal_berita_acara'] = self.tanggal_berita_acara.strftime('%d-%m-%Y')
        if self.tanggal_surat_dipa:
            result['tanggal_surat_dipa'] = self.tanggal_surat_dipa.strftime('%d-%m-%Y')
        
        return result
