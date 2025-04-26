from db import db

class SuratPerintahMulaiKerja(db.Model):
    __tablename__ = 'surat_perintah_mulai_kerja'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('ikram.project.id', ondelete='CASCADE'), nullable=False)
    nomor_spmk = db.Column(db.String(100), nullable=False)
    tanggal_spmk = db.Column(db.Date, nullable=False)
    tanggal_spmk_huruf = db.Column(db.String(255), nullable=False)
    tanggal_mulai_kerja = db.Column(db.Date, nullable=False)
    waktu_penyelesaian = db.Column(db.Date, nullable=False)
    ruanglingkup_pekerjaan = db.Column(db.Text)

    rentang_hari_pengerjaan = db.Column(db.Text, nullable=True)
    rentang_hari_pengerjaan_huruf = db.Column(db.Text, nullable=True)
    denda_pengerjaan = db.Column(db.Text, nullable=True)

    
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    project = db.relationship('Project', backref=db.backref('surat_perintah_mulai_kerja', cascade='all, delete-orphan'), lazy=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
