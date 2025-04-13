from db import db

class BeritaAcaraPembayaranTahap(db.Model):
    __tablename__ = 'berita_acara_pembayaran_tahap'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    nama_termin_tahap_ke = db.Column(db.String(255), nullable=True)
    jumlah_nilai_kontrak_jumlah_total = db.Column(db.Numeric, nullable=True)
    jumlah_nilai_kontrak_huruf = db.Column(db.String(255), nullable=True)
    jumlah_uang_yang_harus_dibayarkan = db.Column(db.Numeric, nullable=True)
    jumlah_uang_yang_harus_dibayarkan_huruf = db.Column(db.String(255), nullable=True)
    tahap_ke_terbilang = db.Column(db.Text, nullable=True)
    pembayaran_bulan = db.Column(db.Text, nullable=True)  # Kolom baru

    # Relasi dengan tabel Project
    project = db.relationship('Project', backref=db.backref('berita_acara_pembayaran_tahap', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
