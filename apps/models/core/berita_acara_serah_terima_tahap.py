from datetime import datetime
from db import db

class BeritaAcaraSerahTerimaTahap(db.Model):
    __tablename__ = 'berita_acara_serah_terima_tahap'
    __table_args__ = {'schema': 'ikram'}

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)

    tahap_ke = db.Column(db.Integer, nullable=True)
    tahap_ke_terbilang = db.Column(db.String(255), nullable=True)
    nomor_bap_serahterima = db.Column(db.String(255), nullable=True)
    tanggal_bap_serahterima = db.Column(db.Date, nullable=True)
    tanggal_bap_serahterima_terbilang = db.Column(db.String(255), nullable=True)
    untuk_bulan = db.Column(db.String(255), nullable=True)
    persentase_pekerjaan = db.Column(db.String(255), nullable=True)
    nilai_kontrak = db.Column(db.Integer, nullable=True)
    nilai_kontrak_terbilang = db.Column(db.String(255), nullable=True)
    nomor_surat_dipa = db.Column(db.String(255), nullable=True)
    tanggal_surat_dipa = db.Column(db.Date, nullable=True)
    nilai_pembayaran = db.Column(db.Integer, nullable=True)
    nilai_pembayaran_terbilang = db.Column(db.String(255), nullable=True)

    uraian_pekerjaan = db.Column(db.ARRAY(db.String), nullable=True)
    satuan_ukuran = db.Column(db.ARRAY(db.String), nullable=True)
    jumlah = db.Column(db.ARRAY(db.String), nullable=True)
    keterangan = db.Column(db.ARRAY(db.String), nullable=True)

    project = db.relationship('Project', backref=db.backref('berita_acara_tahap', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        result = {column.name: getattr(self, column.name) for column in self.__table__.columns}

        # Format tanggal jadi DD-MM-YYYY
        if self.tanggal_bap_serahterima:
            result['tanggal_bap_serahterima'] = self.tanggal_bap_serahterima.strftime('%d-%m-%Y')
        if self.tanggal_surat_dipa:
            result['tanggal_surat_dipa'] = self.tanggal_surat_dipa.strftime('%d-%m-%Y')

        return result
