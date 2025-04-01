from datetime import datetime
from db import db

class BeritaAcaraSerahTerimaPekerjaanPerencanaan(db.Model):
    __tablename__ = 'berita_acara_serah_terima_pekerjaan_perencanaan'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    nomor_surat_berita_acara = db.Column(db.String(255), nullable=True)
    tanggal_surat_berita_acara = db.Column(db.Date, nullable=True)
    tanggal_surat_berita_acara_huruf = db.Column(db.String(255), nullable=True)
    nomor_surat_perintah_kerja = db.Column(db.String(255), nullable=True)
    tanggal_surat_perintah_kerja = db.Column(db.Date, nullable=True)
    
    # Kolom yang dihapus berdasarkan revisi
    # persentase_pekerjaan - dihapus
    # nomor_surat_kontrak - dihapus
    # tanggal_surat_kontrak - dihapus
    
    nomor_surat_dipa = db.Column(db.String(255), nullable=True)  
    tanggal_surat_dipa = db.Column(db.Date, nullable=True)  
    
    nilai_kontrak_angka = db.Column(db.Numeric, nullable=True)
    nilai_kontrak_huruf = db.Column(db.String(255), nullable=True)
    waktu_mulai = db.Column(db.Date, nullable=True)
    waktu_selesai = db.Column(db.Date, nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relasi dengan tabel Project
    project = db.relationship('Project', backref=db.backref('berita_acara_serah_terima_pekerjaan_perencanaan', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        result = {column.name: getattr(self, column.name) for column in self.__table__.columns}

        # Format tanggal menjadi DD-MM-YYYY jika ada
        if self.tanggal_surat_berita_acara:
            result['tanggal_surat_berita_acara'] = self.tanggal_surat_berita_acara.strftime('%d-%m-%Y')
        if self.tanggal_surat_perintah_kerja:
            result['tanggal_surat_perintah_kerja'] = self.tanggal_surat_perintah_kerja.strftime('%d-%m-%Y')
        if self.tanggal_surat_dipa:
            result['tanggal_surat_dipa'] = self.tanggal_surat_dipa.strftime('%d-%m-%Y')
        
        return result
