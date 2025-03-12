from db import db

class LampiranBeritaAcaraSerahTerimaUangMuka(db.Model):
    __tablename__ = 'lampiran_berita_acara_serah_terima_uang_muka'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    judul_lampiran = db.Column(db.String(255), nullable=True)
    nomor = db.Column(db.String(255), nullable=True)
    uraian_pekerjaan = db.Column(db.Text, nullable=True)
    satuan_ukuran = db.Column(db.String(255), nullable=True)
    jumlah = db.Column(db.Numeric, nullable=True)
    keterangan = db.Column(db.Text, nullable=True)

    # Relasi dengan tabel Project
    project = db.relationship('Project', backref=db.backref('lampiran_berita_acara_serah_terima_uang_muka', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
