from db import db

class SyaratSyaratKhususKontrak(db.Model):
    __tablename__ = 'syarat_syarat_khusus_kontrak'
    __table_args__ = {'schema': 'ikram'}

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)

    ketentuan = db.Column(db.Text)
    pengaturan_dalam_sskk = db.Column(db.Text)
    
    # ✅ Tambahan kolom baru
    website_pihak_1 = db.Column(db.Text)
    fax_pihak_1 = db.Column(db.Text)
    website_pihak_2 = db.Column(db.Text)
    fax_pihak_2 = db.Column(db.Text)
    masa_pemeliharaan_terbilang = db.Column(db.Text)
    waktu_penyerahan_gambar = db.Column(db.Text)
    penyesuaian_harga = db.Column(db.Text)
    pembayaran_tagihan = db.Column(db.Text)
    persetujuan_tindakan_penyedia = db.Column(db.Text)
    persetujuan_tindakan_pengawas = db.Column(db.Text)
    besaran_uangmuka = db.Column(db.Text)
    dokumen_tagihan_prestasi = db.Column(db.ARRAY(db.String))
    pembayaran_bahan_peralatan = db.Column(db.ARRAY(db.String))
    umur_konstruksi_gagal_bangunan = db.Column(db.ARRAY(db.String))
    perselisihan_sengketa = db.Column(db.Text)

    # 🔄 Kolom yang diupdate
    ketentuan_masa_pelaksanaan = db.Column(db.ARRAY(db.String))  # rename dari bagian_pekerjaan
    ketentuan_masa_pemeliharaan = db.Column(db.ARRAY(db.String))  # rename dari masa_pemeliharaan_pekerjaan
    masukan_gambar_proyek = db.Column(db.ARRAY(db.String))  # diubah dari text ke array
    masa_pelaksanaan_pekerjaan = db.Column(db.String)  # diubah dari array ke string
    hak_dan_kewajiban_penyedia = db.Column(db.ARRAY(db.String))  # diubah dari text ke array

    # ❌ Kolom yang dihapus
    # pasal_dalam_sskk = Dihapus
    # bagian_pekerjaan_2 = Dihapus
    # waktu_pedoman_pengoperasian_huruf = Dihapus
    # no_table_pembayaran_prestasi_pekerjaan = Dihapus
    # persentase_pembayaran_bahan_baku_table_pembayaran_bahan_peralatan = Dihapus
    # no_table_2_daftar_harga_satuan = Dihapus
    # no_table_3_pekerjaan_utama = Dihapus
    # no_table_4_pekerjaan_bukan_pekerjaan_utama = Dihapus
    # no_table_5_daftar_personel_manajerial = Dihapus
    # no_table_6_daftar_personel_manajerial = Dihapus

    masa_pemeliharaan = db.Column(db.String(255))
    list_serah_terima_pekerjaan = db.Column(db.ARRAY(db.String))
    waktu_pedoman_pengoperasian = db.Column(db.String(255))

    keterangan_kepemilikan_dokumen = db.Column(db.Text)
    fasilitas = db.Column(db.Text)
    peristiwa_kompensasi = db.Column(db.Text)

    tahapan_pembayaran_table_pembayaran_prestasi_pekerjaan = db.Column(db.ARRAY(db.String))
    besaran_persen_pembayaran_table_pembayaran_prestasi_pekerjaan = db.Column(db.ARRAY(db.String))
    keterangan_pembayaran_table_pembayaran_prestasi_pekerjaan = db.Column(db.ARRAY(db.String))

    # ✅ disederhanakan namanya
    # nama_bahan_baku_table_pembayaran_bahan_peralatan dan persentase_... diganti menjadi pembayaran_bahan_peralatan di atas

    # Table 2
    mata_pembayaran_table_2_daftar_harga_satuan = db.Column(db.ARRAY(db.String))
    kuantitas_table_2_daftar_harga_satuan = db.Column(db.ARRAY(db.String))
    harga_satuan_hps_table_2_daftar_harga_satuan = db.Column(db.ARRAY(db.String))
    harga_satuan_penawaran_table_2_daftar_harga_satuan = db.Column(db.ARRAY(db.String))
    persen_terhadap_hps_table_2_daftar_harga_satuan = db.Column(db.ARRAY(db.String))
    keterangan_table_2_daftar_harga_satuan = db.Column(db.ARRAY(db.String))

    # Table 3
    bagian_pekerjaan_yang_disubkontrakan_table_3_pekerjaan_utama = db.Column(db.ARRAY(db.String))
    nama_subkontraktor_table_3_pekerjaan_utama = db.Column(db.ARRAY(db.String))
    alamat_subkontraktor_table_3_pekerjaan_utama = db.Column(db.ARRAY(db.String))
    kualifikasi_subkontraktor_table_3_pekerjaan_utama = db.Column(db.ARRAY(db.String))
    keterangan_table_3_pekerjaan_utama = db.Column(db.ARRAY(db.String))

    # Table 4
    bagian_pekerjaan_yang_disubkontrakan_table_4_pekerjaan_bukan_pekerjaan_utama = db.Column(db.ARRAY(db.String))
    nama_subkontraktor_table_4_pekerjaan_bukan_pekerjaan_utama = db.Column(db.ARRAY(db.String))
    alamat_subkontraktor_table_4_pekerjaan_bukan_pekerjaan_utama = db.Column(db.ARRAY(db.String))
    kualifikasi_subkontraktor_table_4_pekerjaan_bukan_pekerjaan_utama = db.Column(db.ARRAY(db.String))
    keterangan_table_4_pekerjaan_bukan_pekerjaan_utama = db.Column(db.ARRAY(db.String))

    # Table 5
    nama_personel_manajerial_table_5_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))
    jabatan_dalam_pekerjaan_table_5_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))
    tingkat_pendidikan_ijazah_table_5_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))
    pengalaman_kerja_professional_table_5_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))
    sertifikat_kompetensi_kerja_table_5_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))
    keterangan_table_5_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))

    # Table 6
    nama_peralatan_utama_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))
    merek_dan_tipe_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))
    kapasitas_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))
    jumlah_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))
    kondisi_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))
    status_kepemilikan_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))
    keterangan_table_6_daftar_personel_manajerial = db.Column(db.ARRAY(db.String))

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    project = db.relationship('Project', backref=db.backref('syarat_syarat_khusus_kontrak', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
