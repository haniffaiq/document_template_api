from db import db
from datetime import date

class RingkasanKontrak(db.Model):
    __tablename__ = 'ringkasan_kontrak'
    __table_args__ = {'schema': 'ikram'}

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    nomor_dipa = db.Column(db.String(255), nullable=True)
    tanggal_dipa = db.Column(db.Date, nullable=True)
    kode_kegiatan_sub_kegiatan_mak = db.Column(db.String(255), nullable=True)
    perihal_keterangan = db.Column(db.Text, nullable=True)
    nilai_kontrak_angka = db.Column(db.Numeric, nullable=True)
    nilai_kontrak_huruf = db.Column(db.String(255), nullable=True)
    jangka_waktu_pelaksanaan = db.Column(db.Integer, nullable=True)
    ketentuan_sanksi = db.Column(db.Text, nullable=True)
    dalam_rangka_pembayaran = db.Column(db.Text, nullable=True)
    nomor_ringkasan_kontrak = db.Column(db.String(255), nullable=True)

    # ✅ Kolom tambahan
    nominal_pembayaran_angka = db.Column(db.Integer, nullable=True)
    nominal_pembayaran_huruf = db.Column(db.Text, nullable=True)
    jangka_waktu_pelaksanaan_huruf = db.Column(db.Text, nullable=True)
    tanggal_ringkasan_kontrak = db.Column(db.Date, nullable=True)


    project = db.relationship('Project', backref=db.backref('ringkasan_kontrak', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        result = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        if self.tanggal_dipa:
            result['tanggal_dipa'] = self.tanggal_dipa.strftime('%d-%m-%Y')
        if self.tanggal_ringkasan_kontrak:
            result['tanggal_ringkasan_kontrak'] = self.tanggal_ringkasan_kontrak.strftime('%d-%m-%Y')
        return result
