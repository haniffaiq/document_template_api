from datetime import datetime
from db import db

class Project(db.Model):
    __tablename__ = 'project'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(255), nullable=True)
    nomor_surat_bap = db.Column(db.String(255), nullable=True)
    tanggal_surat_bap = db.Column(db.Date, nullable=True)  # Ubah menjadi Date
    tanggal_surat_bap_huruf = db.Column(db.String(255), nullable=True)
    nomor_berita_acara_pemeriksaan_pekerjaan = db.Column(db.String(255), nullable=True)
    tanggal_berita_acara_pemeriksaan_pekerjaan = db.Column(db.Date, nullable=True)  # Ubah menjadi Date
    tanggal_berita_acara_pemeriksaan_pekerjaan_huruf = db.Column(db.String(255), nullable=True)
    nomor_surat_penunjukan_penyedia_barang_jasa_sppbj = db.Column(db.String(255), nullable=True)
    tanggal_surat_penunjukan_penyedia_barang_jasa_sppbj = db.Column(db.Date, nullable=True)  # Ubah menjadi Date
    tanggal_surat_penunjukan_penyedia_barang_jasa_sppbj_huruf = db.Column(db.String(255), nullable=True)
    nomor_surat_perjanjian_kontrak = db.Column(db.String(255), nullable=True)
    tanggal_surat_perjanjian_kontrak = db.Column(db.Date, nullable=True)  # Ubah menjadi Date
    hari_dan_tanggal_surat_pernyataan_angka = db.Column(db.String(255), nullable=True)
    
    # Pihak 1 (Ubah menjadi lebih spesifik jika perlu)
    nama_pihak_1 = db.Column(db.String(255), nullable=True)
    nip_pihak_1 = db.Column(db.String(255), nullable=True)
    email_pihak_1 = db.Column(db.String(255), nullable=True)
    pangkat_golongan_ruang_pihak_1 = db.Column(db.String(255), nullable=True)
    jabatan_pihak_1 = db.Column(db.String(255), nullable=True)
    perusahaan_pihak_1 = db.Column(db.String(255), nullable=True)
    alamat_pihak_1 = db.Column(db.String(255), nullable=True)
    deskripsi_ttd_pihak_1 = db.Column(db.String(255), nullable=True)
    nomor_kontak_pihak_1 = db.Column(db.String(255), nullable=True)
    
    # Pihak 2
    nama_pihak_2 = db.Column(db.String(255), nullable=True)
    alamat_pihak_2 = db.Column(db.String(255), nullable=True)
    email_pihak_2 = db.Column(db.String(255), nullable=True)
    perusahaan_pihak_2 = db.Column(db.String(255), nullable=True)
    jabatan_pihak_2 = db.Column(db.String(255), nullable=True)
    nama_bank_pihak_2 = db.Column(db.String(255), nullable=True)
    nomor_rekening_pihak_2 = db.Column(db.String(255), nullable=True)
    npwp_pihak_2 = db.Column(db.String(255), nullable=True)
    nip_pihak_2 = db.Column(db.String(255), nullable=True)
    deskripsi_ttd_pihak_2 = db.Column(db.String(255), nullable=True)
    nomor_akta_notaris_pihak_2 = db.Column(db.String(255), nullable=True)
    tanggal_nomor_akta_notaris_pihak_2 = db.Column(db.Date, nullable=True)  # Ubah menjadi Date
    nomor_kontak_pihak_2 = db.Column(db.String(255), nullable=True)
    
    # Detail Pekerjaan
    lokasi_pekerjaan = db.Column(db.String(255), nullable=True)
    pekerjaan = db.Column(db.String(255), nullable=True)
    nominal_pembayaran_angka = db.Column(db.Float, nullable=True)
    nominal_pembayaran_huruf = db.Column(db.String(255), nullable=True)
    tempat_ttd = db.Column(db.String(255), nullable=True)
    ruang_lingkup_pekerjaan = db.Column(db.String(255), nullable=True)
    denda_akibat_keterlambatan = db.Column(db.Float, nullable=True)
    nama_notaris_pihak_2 = db.Column(db.String(255), nullable=True)
    
    # Kolom Baru yang Diperlukan
    nomor_rekening_pihak_1 = db.Column(db.String(255), nullable=True)  # Kolom untuk nomor rekening pihak 1
    nama_bank_pihak_1 = db.Column(db.String(255), nullable=True)  # Kolom untuk nama bank pihak 1

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        # Mengembalikan data dalam bentuk dictionary
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
