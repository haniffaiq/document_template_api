from db import db

class SyaratSyaratKhususKontrak(db.Model):
    __tablename__ = 'syarat_syarat_khusus_kontrak'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    pasal_dalam_sskk = db.Column(db.String(255))
    ketentuan = db.Column(db.Text)
    pengaturan_dalam_sskk = db.Column(db.Text)
    masa_pelaksanaan_pekerjaan = db.Column(db.ARRAY(db.String))  # Array of strings
    bagian_pekerjaan = db.Column(db.ARRAY(db.String))  # Array of strings
    masa_pemeliharaan = db.Column(db.String(255))
    list_serah_terima_pekerjaan = db.Column(db.ARRAY(db.String))  # Array of strings
    masa_pemeliharaan_pekerjaan = db.Column(db.ARRAY(db.String))  # Array of strings
    bagian_pekerjaan_2 = db.Column(db.ARRAY(db.String))  # Array of strings
    masukan_gambar_proyek = db.Column(db.Text)  # Optional, could be NULL
    waktu_pedoman_pengoperasian = db.Column(db.String(255))
    waktu_pedoman_pengoperasian_huruf = db.Column(db.String(255))
    hak_dan_kewajiban_penyedia = db.Column(db.Text)
    keterangan_kepemilikan_dokumen = db.Column(db.Text)
    fasilitas = db.Column(db.Text)
    peristiwa_kompensasi = db.Column(db.Text)
    no_table_pembayaran_prestasi_pekerjaan = db.Column(db.String(255))
    tahapan_pembayaran_table_pembayaran_prestasi_pekerjaan = db.Column(db.ARRAY(db.String))  # Array of strings
    besaran_persen_pembayaran_table_pembayaran_prestasi_pekerjaan = db.Column(db.ARRAY(db.String))  # Array of strings
    keterangan_pembayaran_table_pembayaran_prestasi_pekerjaan = db.Column(db.ARRAY(db.String))  # Array of strings
    nama_bahan_baku_table_pembayaran_bahan_peralatan = db.Column(db.ARRAY(db.String))  # Array of strings
    persentase_pembayaran_bahan_baku_table_pembayaran_bahan_peralatan = db.Column(db.ARRAY(db.String))  # Array of strings
    no_table_2_daftar_harga_satuan = db.Column(db.String(255))
    mata_pembayaran_table_2_daftar_harga_satuan = db.Column(db.ARRAY(db.String))  # Array of strings
    kuantitas_table_2_daftar_harga_satuan = db.Column(db.ARRAY(db.String))  # Array of strings
    harga_satuan_hps_table_2_daftar_harga_satuan = db.Column(db.ARRAY(db.String))  # Array of strings
    harga_satuan_penawaran_table_2_daftar_harga_satuan = db.Column(db.ARRAY(db.String))  # Array of strings
    persen_terhadap_hps_table_2_daftar_harga_satuan = db.Column(db.ARRAY(db.String))  # Array of strings
    keterangan_table_2_daftar_harga_satuan = db.Column(db.ARRAY(db.String))  # Array of strings
    no_table_3_pekerjaan_utama = db.Column(db.String(255))
    bagian_pekerjaan_yang_disubkontrakan_table_3_pekerjaan_utama = db.Column(db.ARRAY(db.String))  # Array of strings
    nama_subkontraktor_table_3_pekerjaan_utama = db.Column(db.ARRAY(db.String))  # Array of strings
    alamat_subkontraktor_table_3_pekerjaan_utama = db.Column(db.ARRAY(db.String))  # Array of strings
    kualifikasi_subkontraktor_table_3_pekerjaan_utama = db.Column(db.ARRAY(db.String))  # Array of strings
    keterangan_table_3_pekerjaan_utama = db.Column(db.ARRAY(db.String))  # Array of strings
    no_table_4_pekerjaan_bukan_pekerjaan_utama = db.Column(db.String(255))
    bagian_pekerjaan_yang_disubkontrakan_table_4_pekerjaan_bukan_pekerjaan_utama = db.Column(db.ARRAY(db.String))  # Array of strings
    nama_subkontraktor_table_4_pekerjaan_bukan_pekerjaan_utama = db.Column(db.ARRAY(db.String))  # Array of strings
    alamat_subkontraktor_table_4_pekerjaan_bukan_pekerjaan_utama = db.Column(db.ARRAY(db.String))  # Array of strings
    kualifikasi_subkontraktor_table_4_pekerjaan_bukan_pekerjaan_utama = db.Column(db.ARRAY(db.String))  # Array of strings
    keterangan_table_4_pekerjaan_bukan_pekerjaan_utama = db.Column(db.ARRAY(db.String))  # Array of strings
    no_table_5_daftar_personel_manajerial = db.Column(db.String(255))
    nama_personel_manajerial_table_5_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))  # Array of strings
    jabatan_dalam_pekerjaan_table_5_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))  # Array of strings
    tingkat_pendidikan_ijazah_table_5_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))  # Array of strings
    pengalaman_kerja_professional_table_5_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))  # Array of strings
    sertifikat_kompetensi_kerja_table_5_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))  # Array of strings
    keterangan_table_5_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))  # Array of strings
    no_table_6_daftar_personel_manajerial = db.Column(db.String(255))
    nama_peralatan_utama_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))  # Array of strings
    merek_dan_tipe_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))  # Array of strings
    kapasitas_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))  # Array of strings
    jumlah_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))  # Array of strings
    kondisi_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))  # Array of strings
    status_kepemilikan_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))  # Array of strings
    keterangan_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))  # Array of strings
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    project = db.relationship('Project', backref=db.backref('syarat_syarat_khusus_kontrak', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}