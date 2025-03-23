from db import db


class LampiranBeritaAcaraPemeriksaanTahapKe(db.Model):
    __tablename__ = 'lampiran_berita_acara_pemeriksaan_tahap_ke'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    judul_lampiran = db.Column(db.String(255), nullable=False)
    nomor = db.Column(db.String(100), nullable=False)
    uraian_pekerjaan = db.Column(db.Text, nullable=False)
    satuan_ukuran = db.Column(db.String(50), nullable=False)
    jumlah = db.Column(db.Numeric(15, 2), nullable=False)
    keterangan = db.Column(db.Text)
    jumlah_ubah = db.Column(db.Boolean, default=False)  # Opsi untuk mengubah jumlah
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    project = db.relationship('Project', backref=db.backref('lampiran_berita_acara_pemeriksaan_tahap_ke', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
