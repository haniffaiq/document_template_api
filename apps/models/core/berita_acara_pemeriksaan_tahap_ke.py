from db import db


class BeritaAcaraPemeriksaanTahapKe(db.Model):
    __tablename__ = 'berita_acara_pemeriksaan_tahap_ke'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    nomor_berita_acara = db.Column(db.String(100), nullable=False)
    tanggal_berita_acara = db.Column(db.Date, nullable=False)
    tanggal_berita_acara_huruf = db.Column(db.String(255), nullable=False)
    deskripsi_pemeriksaan = db.Column(db.Text)
    nilai_kontrak_angka = db.Column(db.Numeric(15, 2), nullable=False)
    nilai_kontrak_huruf = db.Column(db.String(255), nullable=False)
    rentang_pengerjaan_huruf = db.Column(db.String(255))
    jenis_pekerjaan = db.Column(db.ARRAY(db.String), nullable=False)  # Array untuk jenis pekerjaan
    
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    project = db.relationship('Project', backref=db.backref('berita_acara_pemeriksaan_tahap_ke', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
