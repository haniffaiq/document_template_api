from datetime import datetime
from db import db

class BeritaAcaraPemeriksaanTahapKe(db.Model):
    __tablename__ = 'berita_acara_pemeriksaan_tahap_ke'
    __table_args__ = {'schema': 'ikram'}
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(
        db.Integer,
        db.ForeignKey('ikram.project.id', ondelete='CASCADE'),
        nullable=False
    )

    nomor_berita_acara = db.Column(db.String(255), nullable=True)
    tanggal_berita_acara = db.Column(db.Date, nullable=True)
    tanggal_berita_acara_huruf = db.Column(db.String(255), nullable=True)
    nilai_kontrak_angka = db.Column(db.Numeric, nullable=True)
    nilai_kontrak_huruf = db.Column(db.String(255), nullable=True)

    jenis_pekerjaan = db.Column(db.ARRAY(db.String), nullable=True)
    jumlah = db.Column(db.ARRAY(db.Integer), nullable=True)
    satuan_pekerjaan = db.Column(db.ARRAY(db.String), nullable=True)
    keterangan = db.Column(db.ARRAY(db.String), nullable=True)

    # Kolom tambahan sesuai revisi
    tanggal_awal = db.Column(db.Date, nullable=True)
    tanggal_akhir = db.Column(db.Date, nullable=True)
    deskripsi_pemeriksaan = db.Column(db.Text, nullable=True)

    tahap = db.Column(db.String(255), nullable=True)
    tahap_terbilang = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # Relasi ke tabel project
    project = db.relationship(
        'Project',
        backref=db.backref('berita_acara_pemeriksaan_tahap_ke', cascade='all, delete-orphan'),
        lazy=True
    )

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def as_dict(self):
        result = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        
        # Format tanggal ke DD-MM-YYYY
        for field in ['tanggal_berita_acara', 'tanggal_awal', 'tanggal_akhir']:
            if getattr(self, field):
                result[field] = getattr(self, field).strftime('%d-%m-%Y')
        
        return result
