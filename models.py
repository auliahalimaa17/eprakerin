from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# User Table
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    roles = db.Column(db.String(50), nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    nohp = db.Column(db.String(20), nullable=False)

    def __init__(self, email, password, roles, nama, nohp):
        self.email = email
        self.password = password
        self.roles = roles
        self.nama = nama
        self.nohp = nohp


# Data Peserta Table
class DataPeserta(db.Model):
    __tablename__ = 'data_peserta'
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    nohp = db.Column(db.String(20), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    asal_kampus = db.Column(db.String(100), nullable=False)
    jenis_kelamin = db.Column(db.String(50), nullable=False)
    tempat_tanggal_lahir = db.Column(db.String(100), nullable=False)
    tanggal_dimulai = db.Column(db.Date, nullable=False)
    tanggal_berakhir = db.Column(db.Date, nullable=False)
    nama_pembimbing = db.Column(db.String(100), nullable=True)
    nohp_pembimbing = db.Column(db.String(20), nullable=True)

    user = db.relationship('User', backref=db.backref('peserta', lazy=True))

    def __repr__(self):
        return f"<DataPeserta {self.nama}>"


# Berkas Peserta Table
class BerkasPeserta(db.Model):
    __tablename__ = 'berkas_peserta'
    id = db.Column(db.Integer, primary_key=True)
    id_peserta = db.Column(db.Integer, db.ForeignKey('data_peserta.id', ondelete='CASCADE'), nullable=False)
    surat_pengantar_magang = db.Column(db.String(255), nullable=True)
    proposal_magang = db.Column(db.String(255), nullable=True)
    curriculum_vitae = db.Column(db.String(255), nullable=True)
    surat_pembuatan_idcard = db.Column(db.String(255), nullable=True)
    surat_penerimaan = db.Column(db.String(255), nullable=True)
    pas_foto = db.Column(db.String(255), nullable=True)
    surat_sehat = db.Column(db.String(255), nullable=True)
    kartu_tanda_mahasiswa = db.Column(db.String(255), nullable=True)
    ktp = db.Column(db.String(255), nullable=True)
    kartu_keluarga = db.Column(db.String(255), nullable=True)
    sim = db.Column(db.String(255), nullable=True)
    stnk = db.Column(db.String(255), nullable=True)
    skck = db.Column(db.String(255), nullable=True)

    peserta = db.relationship('DataPeserta', backref=db.backref('berkas', lazy=True))

    def __repr__(self):
        return f"<BerkasPeserta {self.id_peserta}>"


# Status Pendaftaran Table
class StatusPendaftaran(db.Model):
    __tablename__ = 'status_pendaftaran'
    id = db.Column(db.Integer, primary_key=True)
    id_peserta = db.Column(db.Integer, db.ForeignKey('data_peserta.id', ondelete='CASCADE'), nullable=False)
    status_daftar = db.Column(db.String(50), nullable=False)
    nama_divisi = db.Column(db.String(50), nullable=True)
    status_berkas = db.Column(db.String(50), nullable=True)
    catatan = db.Column(db.Text, nullable=True)
    tanggal_wawancara = db.Column(db.Date, nullable=True)

    peserta = db.relationship('DataPeserta', backref=db.backref('status', lazy=True))

    def __repr__(self):
        return f"<StatusPendaftaran {self.status_daftar}>"


# Data Berkas HC Table
class DataBerkasHC(db.Model):
    __tablename__ = 'data_berkas_hc'
    id = db.Column(db.Integer, primary_key=True)
    template_surat_pembuatan_idcard = db.Column(db.String(255), nullable=True)
    template_surat_penerimaan_prakerin = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<DataBerkasHC {self.id}>"
