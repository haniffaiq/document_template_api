from db import db

class SuratPenunjukanPenyediaBarangJasa(db.Model):
    __tablename__ = 'surat_penunjukan_penyedia_barang_jasa'
    __table_args__ = {'schema': 'ikram'}

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    kode_tender_id_packet = db.Column(db.String(100))
    nilai_penawaran = db.Column(db.Numeric(15, 2))
    nilai_terkoreksi = db.Column(db.Numeric(15, 2))
    nilai_final = db.Column(db.Numeric(15, 2))
    nilai_jaminan_pelaksanaan_angka = db.Column(db.Numeric(15, 2))
    nilai_jaminan_pelaksanaan_huruf = db.Column(db.String(255))
    jangka_waktu_pekerjaan_angka = db.Column(db.Integer)
    jangka_waktu_pekerjaan_huruf = db.Column(db.String(255))
    uu_pp_aturan_sanksi = db.Column(db.String(255))
    tembusan = db.Column(db.ARRAY(db.Text), nullable=True)  # <- Ini diubah menjadi ARRAY of TEXT

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # Definisikan relasi dengan Project
    project = db.relationship('Project', backref=db.backref('surat_penunjukan_penyedia_barang_jasa', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
