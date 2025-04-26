from db import db

class BeritaAcaraSerahTerimaPekerjaanPengawasan(db.Model):
    __tablename__ = 'berita_acara_serah_terima_pekerjaan_pengawasan'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    nomor_surat_berita_acara = db.Column(db.String(100), nullable=False)
    tanggal_surat_berita_acara = db.Column(db.Date, nullable=False)
    tanggal_surat_berita_acara_huruf = db.Column(db.String(255), nullable=False)
    nomor_surat_perintah_kerja = db.Column(db.String(100), nullable=False)
    tanggal_surat_perintah_kerja = db.Column(db.Date, nullable=False)
    nomor_surat_dipa = db.Column(db.String(100), nullable=False)
    tanggal_surat_dipa = db.Column(db.Date, nullable=False)
    nilai_kontrak_angka = db.Column(db.Numeric(15, 2), nullable=False)
    nilai_kontrak_huruf = db.Column(db.String(255), nullable=False)
    waktu_mulai = db.Column(db.Date, nullable=False)
    waktu_selesai = db.Column(db.Date, nullable=False)
    
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    project = db.relationship('Project', backref=db.backref('berita_acara_serah_terima_pekerjaan_pengawasan', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
