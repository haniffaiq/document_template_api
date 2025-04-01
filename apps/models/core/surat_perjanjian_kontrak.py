from db import db

class SuratPerjanjianKontrak(db.Model):
    __tablename__ = 'surat_perjanjian_kontrak'
    __table_args__ = {'schema': 'ikram'}

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)  # Pastikan ForeignKey didefinisikan dengan benar
    tempat_surat_perjanjian_kontrak = db.Column(db.String(255))
    paket_pekerjaan = db.Column(db.String(255))
    nomor_surat_berita_acara_hasil_pemilihan_nomor = db.Column(db.String(100))
    tanggal_nomor_surat_berita_acara_hasil_pemilihan_nomor = db.Column(db.Date)
    pp_uu_aturan_tertentu = db.Column(db.String(255))
    nama_pemilik_rekening_pihak_2 = db.Column(db.String(255))
    total_harga_angka = db.Column(db.Numeric(15, 2))
    total_harga_huruf = db.Column(db.String(255))
    kode_akun_kegiatan = db.Column(db.String(100))
    tanggal_penyerahan_pertama_pekerjaan_angka = db.Column(db.Date)
    tanggal_penyerahan_pertama_pekerjaan_huruf = db.Column(db.String(255))
    tanggal_penyerahan_akhir_pekerjaan_angka = db.Column(db.Date)
    tanggal_penyerahan_akhir_pekerjaan_huruf = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # Definisikan relasi dengan Project
    project = db.relationship('Project', backref=db.backref('surat_perjanjian_kontrak', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
