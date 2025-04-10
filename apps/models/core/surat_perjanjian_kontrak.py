from db import db

class SuratPerjanjianKontrak(db.Model):
    __tablename__ = 'surat_perjanjian_kontrak'
    __table_args__ = {'schema': 'ikram'}

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)

    tanggal_nomor_surat_berita_acara_hasil_pemilihan_nomor = db.Column(db.Date)

    total_harga_angka = db.Column(db.Numeric)
    total_harga_huruf = db.Column(db.String)
    kode_akun_kegiatan = db.Column(db.String)

    masa_pelaksanaan_pekerjaan = db.Column(db.Text)
    masa_pelaksanaan_pekerjaan_huruf = db.Column(db.Text)
    masa_pemeliharaan_pekerjaan = db.Column(db.Text)
    masa_pemeliharaan_pekerjaan_huruf = db.Column(db.Text)

    ketentuan_persetujuan = db.Column(db.ARRAY(db.String))
    ruang_lingkup_pekerjaan = db.Column(db.ARRAY(db.String))
    ketentuan_hierarki = db.Column(db.ARRAY(db.String))
    nomor_surat_keputusan_rektor = db.Column(db.Text)
    tanggal_surat_keputusan_rektor = db.Column(db.Date)
    rincian_surat_keputusan = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    project = db.relationship('Project', backref=db.backref('surat_perjanjian_kontrak', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
