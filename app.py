from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
from models import db, User, DataPeserta, BerkasPeserta, StatusPendaftaran, DataBerkasHC
from flask import Flask, redirect, url_for, session
from werkzeug.utils import secure_filename
from datetime import timedelta, datetime
import logging
from io import BytesIO
from fpdf import FPDF
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/dbprakerin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=30)
# Konfigurasi folder upload dan ekstensi yang diizinkan
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file):
    if file and allowed_file(file.filename):
        if file.content_length > MAX_FILE_SIZE:
            raise ValueError('File terlalu besar. Maksimum 2 MB.')
        
        filename = secure_filename(file.filename)
        file_path = os.path.join('uploads', secure_filename(file.filename))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return file_path
    else:
        raise ValueError('Format file tidak valid.')

# Inisialisasi database
db.init_app(app)

# Route halaman login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Cari user berdasarkan email
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            session['user_id'] = user.id
            session['user_role'] = user.roles
            session['user_name'] = user.email
            session['nama'] = user.nama
            session['nohp'] = user.nohp
            session.permanent = True  # Set session permanen sesuai waktu di atas

            flash('Login berhasil!', 'success')

            # Redirect sesuai role user
            if user.roles == 'HC Admin':
                return redirect(url_for('homeadmin'))
            elif user.roles == 'PAM Admin':
                return redirect(url_for('homeadmin'))
            elif user.roles == 'Peserta':
                return redirect(url_for('homepeserta'))
        else:
            flash('Email atau password salah!', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')


# Route halaman registrasi
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        # Validasi: Password dan Konfirmasi Password harus sama
        if password != confirm_password:
            flash('Password dan Konfirmasi Password tidak cocok!', 'danger')
            return redirect(url_for('register'))

        # Tetapkan role sebagai 'Peserta'
        role = 'Peserta'

        try:
            # Buat user baru di tabel User dengan kolom nama dan nohp
            new_user = User(
                email=email,
                password=password,
                roles=role,
                nama=fullname,
                nohp=phone
            )
            db.session.add(new_user)
            db.session.commit()

            # Beri notifikasi sukses dan redirect ke halaman login
            flash('Registrasi akun berhasil dilakukan. Silakan login.', 'success')
            return redirect(url_for('login'))

        except Exception as e:
            db.session.rollback()
            flash(f'Terjadi kesalahan saat registrasi: {str(e)}', 'danger')
            return redirect(url_for('register'))

    return render_template('register.html')


# Route halaman utama peserta
@app.route('/homepeserta')
def homepeserta():
    if 'user_id' not in session or session.get('user_role') != 'Peserta':
        flash('Anda harus login sebagai peserta untuk mengakses halaman ini.', 'warning')
        return redirect(url_for('login'))

    return render_template('home-peserta.html', user_name=session.get('user_name'))

@app.route('/daftarmagang', methods=['GET', 'POST'])
def daftarmagang():
    user_id = session.get('user_id')
    logger.debug(f"User ID dari session: {user_id}")

    # Periksa apakah user sudah login
    if not user_id:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    # Cek status pendaftaran user
    status_pendaftaran = StatusPendaftaran.query.join(DataPeserta).filter(DataPeserta.id_user == user_id).first()
    
    if status_pendaftaran:
        status = status_pendaftaran.status_daftar
        status_berkas = status_pendaftaran.status_berkas
        id_peserta = status_pendaftaran.id_peserta 
        logger.debug(f"Status pendaftaran ditemukan: {status}, ID Peserta: {id_peserta}")
        
        # Redirect berdasarkan status pendaftaran
        if status == 'Perlu Diseleksi':
            return redirect(url_for('prosesseleksi'))
        elif status == 'Kel. Berkas':
            if status_berkas == 'Menunggu Peserta':
                return redirect(url_for('kelengkapanberkas', id=id_peserta))
            elif status_berkas == 'Revisi':
                return redirect(url_for('kelengkapanberkas', id=id_peserta))
            elif status_berkas == 'Sedang Diproses':
                return redirect(url_for('kelengkapanberkasuploaded'))
        elif status == 'Wawancara':
            return redirect(url_for('wawancara', id=id_peserta))
        elif status in ['Diterima', 'Ditolak']:
            return redirect(url_for('pengumuman', id=id_peserta))
            
    if request.method == 'GET':
        user = User.query.filter_by(id=user_id).first()

        if not user:
            flash('Data user tidak ditemukan.', 'danger')
            return redirect(url_for('login'))

        return render_template('daftarmagang.html', user=user)    
    
    elif request.method == 'POST':
        try:
            logger.debug("Memulai proses pendaftaran magang...")
            # Mengambil data dari form
            user_id = session.get('user_id')
            user = User.query.filter_by(id=user_id).first()
            if not user:
                flash('Data user tidak ditemukan.', 'danger')
                return redirect(url_for('login'))
            semester = request.form['semester']
            asal_kampus = request.form['campus']
            jenis_kelamin = request.form['gender']
            tempat_tanggal_lahir = request.form['birth']
            tanggal_dimulai = request.form['startDate']
            tanggal_berakhir = request.form['endDate']
            logger.debug(f"Data form: {semester}, {asal_kampus}, {jenis_kelamin}, {tempat_tanggal_lahir}, {tanggal_dimulai}, {tanggal_berakhir}")

            # Membuat entri baru di tabel data_peserta
            peserta = DataPeserta(
                id_user=user_id,
                nama=user.nama,
                nohp=user.nohp,
                semester=semester,
                asal_kampus=asal_kampus,
                jenis_kelamin=jenis_kelamin,
                tempat_tanggal_lahir=tempat_tanggal_lahir,
                tanggal_dimulai=tanggal_dimulai,
                tanggal_berakhir=tanggal_berakhir,
                nama_pembimbing=None,
                nohp_pembimbing=None
            )
            db.session.add(peserta)
            db.session.commit()
            logger.debug(f"Data peserta berhasil disimpan dengan ID: {peserta.id}")

            # Membuat entri di tabel status_pendaftaran
            status = StatusPendaftaran(
                id_peserta=peserta.id,
                status_daftar='Perlu Diseleksi',
                status_berkas='Sedang Diproses'
            )
            db.session.add(status)
            db.session.commit()
            logger.debug("Status pendaftaran berhasil disimpan.")

            # Menghandle file upload dan menyimpan path file ke tabel berkas_peserta
            file_paths = {}
            for file_key in ['file1', 'file2', 'file3']:
                if file_key in request.files:
                    uploaded_file = request.files[file_key]
                    if uploaded_file.filename != '':
                        file_paths[file_key] = save_file(uploaded_file)
                        logger.debug(f"File {file_key} berhasil diupload: {file_paths[file_key]}")

            berkas = BerkasPeserta(
                id_peserta=peserta.id,
                surat_pengantar_magang=file_paths.get('file1'),
                proposal_magang=file_paths.get('file2'),
                curriculum_vitae=file_paths.get('file3')
            )
            db.session.add(berkas)
            db.session.commit()
            logger.debug(f"Berkas peserta berhasil disimpan.")

            flash('Pendaftaran berhasil! Silakan menunggu proses seleksi.', 'success')
            return redirect(url_for('prosesseleksi'))

        except Exception as e:
            db.session.rollback()
            logger.error(f"Terjadi kesalahan: {str(e)}")
            flash(f'Terjadi kesalahan: {str(e)}', 'danger')
            return redirect(url_for('daftarmagang'))

@app.route('/prosesseleksi')
def prosesseleksi():
    return render_template('proses-seleksi.html')

@app.route('/kelengkapanberkas/<int:id>', methods=['GET', 'POST'])
def kelengkapanberkas(id):
    peserta = db.session.query(DataPeserta, BerkasPeserta, StatusPendaftaran)\
        .join(BerkasPeserta, DataPeserta.id == BerkasPeserta.id_peserta)\
        .join(StatusPendaftaran, DataPeserta.id == StatusPendaftaran.id_peserta)\
        .filter(DataPeserta.id == id).first()

    if request.method == 'POST':
        try:
            # Simpan nama dan no hp pembimbing
            peserta.DataPeserta.nama_pembimbing = request.form['nama_pembimbing']
            peserta.DataPeserta.nohp_pembimbing = request.form['nohp_pembimbing']

            # Handle file uploads
            file_fields = {
                'pas_foto': 'pas_foto',
                'surat_sehat': 'surat_sehat',
                'kartu_tanda_mahasiswa': 'kartu_tanda_mahasiswa',
                'ktp': 'ktp',
                'kartu_keluarga': 'kartu_keluarga',
                'sim': 'sim',
                'stnk': 'stnk',
                'skck': 'skck'
            }

            for field_name, column_name in file_fields.items():
                file = request.files.get(field_name)
                if file and file.filename:
                    filename = secure_filename(file.filename)
                    file_path = os.path.join('uploads', secure_filename(file.filename))
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
                    setattr(peserta.BerkasPeserta, column_name, file_path)

            # Update status pendaftaran dan status berkas
            peserta.StatusPendaftaran.status_berkas = 'Sedang Diproses'
            peserta.StatusPendaftaran.status_daftar = 'Kel. Berkas'

            db.session.commit()
            flash('Berkas berhasil diupload dan status pendaftaran diperbarui.', 'success')
            return redirect(url_for('kelengkapanberkasuploaded'))

        except Exception as e:
            db.session.rollback()
            flash(f'Terjadi kesalahan: {e}', 'danger')

    return render_template('kelengkapan-berkas.html', peserta=peserta)

@app.route('/kelengkapanberkasuploaded')
def kelengkapanberkasuploaded():
    return render_template('kelengkapan-berkas-uploaded.html')

@app.route('/wawancara/<int:id>')
def wawancara(id):
    peserta = db.session.query(DataPeserta, StatusPendaftaran).join(StatusPendaftaran).filter(DataPeserta.id == id).first()
    return render_template('wawancara.html', peserta=peserta)


@app.route('/pengumuman/<int:id>')
def pengumuman(id):
    peserta = (
        db.session.query(DataPeserta, StatusPendaftaran)
        .join(StatusPendaftaran, DataPeserta.id == StatusPendaftaran.id_peserta)
        .filter(StatusPendaftaran.id_peserta == id, StatusPendaftaran.status_daftar == 'Diterima')
        .first()
    )
    
    if not peserta:
        flash('Data peserta tidak ditemukan atau status pendaftaran belum diterima.', 'danger')
        return redirect(url_for('homepeserta'))

    return render_template('pengumuman.html', peserta=peserta)


# Route untuk non peserta

# Route halaman utama admin
@app.route('/homeadmin')
def homeadmin():
    if 'user_id' not in session or session.get('user_role') not in ['HC Admin', 'PAM Admin']:
        flash('Anda harus login sebagai admin untuk mengakses halaman ini.', 'warning')
        return redirect(url_for('login'))

    try:
        # Query jumlah data berdasarkan status
        total_pendaftar = db.session.query(DataPeserta).count()
        total_diterima = db.session.query(StatusPendaftaran).filter_by(status_daftar='Diterima').count()
        total_ditolak = db.session.query(StatusPendaftaran).filter_by(status_daftar='Ditolak').count()
        proses_seleksi = db.session.query(StatusPendaftaran).filter_by(status_daftar='Perlu Diseleksi').count()
        kelengkapan_berkas = db.session.query(StatusPendaftaran).filter_by(status_daftar='Kel. Berkas').count()
        wawancara = db.session.query(StatusPendaftaran).filter_by(status_daftar='Wawancara').count()

        return render_template(
            'home-admin.html',
            user_name=session.get('user_name'),
            total_pendaftar=total_pendaftar,
            total_diterima=total_diterima,
            total_ditolak=total_ditolak,
            proses_seleksi=proses_seleksi,
            kelengkapan_berkas=kelengkapan_berkas,
            wawancara=wawancara
        )

    except Exception as e:
        flash(f"Terjadi kesalahan saat memuat data: {e}", "danger")
        return redirect(url_for('login'))


@app.route('/datapendaftaran')
def datapendaftaran():
    try:
        # Query untuk mengambil data peserta beserta statusnya
        data = (
            db.session.query(
                DataPeserta.id,
                DataPeserta.nama,
                User.email,
                DataPeserta.asal_kampus,
                StatusPendaftaran.status_daftar,
                StatusPendaftaran.status_berkas
            )
            .join(User, DataPeserta.id_user == User.id)
            .join(StatusPendaftaran, DataPeserta.id == StatusPendaftaran.id_peserta)
            .all()
        )
        return render_template('data-pendaftaran.html', data=data)
    except Exception as e:
        logger.error(f"Kesalahan pada route 'datapendaftaran': {e}")
        flash(f"Terjadi kesalahan: {e}", "danger")
        return redirect(url_for('homeadmin'))


@app.route('/detaildatapeserta/<int:id>', methods=['GET', 'POST'])
def detaildatapeserta(id):
    peserta = db.session.query(DataPeserta, StatusPendaftaran, BerkasPeserta)\
        .join(StatusPendaftaran, DataPeserta.id == StatusPendaftaran.id_peserta)\
        .join(BerkasPeserta, DataPeserta.id == BerkasPeserta.id_peserta)\
        .filter(DataPeserta.id == id).first()

    if request.method == 'POST':
        try:
            status_berkas = request.form.get('status-berkas')
            nama_divisi = request.form.get('nama_divisi')
            status_pendaftaran = request.form.get('status-pendaftaran')

            logger.debug(f"Form data diterima: status_berkas={status_berkas}, nama_divisi={nama_divisi}, status_pendaftaran={status_pendaftaran}")

            # Update StatusPendaftaran
            # Jika status berkas adalah "Sesuai", ubah menjadi "Sedang Diproses" sebelum disimpan
            if status_berkas == 'Sesuai':
                peserta.StatusPendaftaran.status_berkas = 'Menunggu Peserta'
            else:
                peserta.StatusPendaftaran.status_berkas = status_berkas
           
            peserta.StatusPendaftaran.status_daftar = status_pendaftaran

            if status_pendaftaran == 'Kel. Berkas':
                peserta.StatusPendaftaran.nama_divisi = nama_divisi

            # Menghandle file upload
            file_tanda_pengenal = request.files.get('surat_tanda_pengenal')
            if file_tanda_pengenal and file_tanda_pengenal.filename:
                file_path_tanda_pengenal = save_file(file_tanda_pengenal)
                peserta.BerkasPeserta.surat_pembuatan_idcard = file_path_tanda_pengenal
                logger.debug(f"File surat tanda pengenal berhasil disimpan: {file_path_tanda_pengenal}")

            file_penerimaan = request.files.get('surat_penerimaan')
            if file_penerimaan and file_penerimaan.filename:
                file_path_penerimaan = save_file(file_penerimaan)
                peserta.BerkasPeserta.surat_penerimaan = file_path_penerimaan
                logger.debug(f"File surat penerimaan berhasil disimpan: {file_path_penerimaan}")

            else:
                # Null-kan jika status berkas bukan "Sesuai"
                peserta.StatusPendaftaran.nama_divisi = None
                peserta.BerkasPeserta.surat_pembuatan_idcard = None
                peserta.BerkasPeserta.surat_penerimaan = None        
            
            db.session.commit()
            flash('Status berhasil diperbarui.', 'success')
            logger.debug("Status pendaftaran berhasil diperbarui.")
            return redirect(url_for('datapendaftaran'))

        except Exception as e:
            db.session.rollback()
            logger.error(f"Terjadi kesalahan saat memperbarui status: {e}")
            flash(f"Terjadi kesalahan: {e}", 'danger')
    return render_template('detail-datapeserta.html', peserta=peserta)


@app.route('/detaildatapesertakelberkas/<int:id>', methods=['GET', 'POST'])
def detaildatapesertakelberkas(id):
    peserta = db.session.query(DataPeserta, StatusPendaftaran, BerkasPeserta)\
        .join(StatusPendaftaran, DataPeserta.id == StatusPendaftaran.id_peserta)\
        .join(BerkasPeserta, DataPeserta.id == BerkasPeserta.id_peserta)\
        .filter(DataPeserta.id == id).first()

    if request.method == 'POST':
        try:
            status_berkas = request.form.get('status-berkas')
            status_pendaftaran = request.form.get('status-pendaftaran')
            catatan = request.form.get('catatan')
            logger.debug(f"Form data diterima: status_berkas={status_berkas}, status_pendaftaran={status_pendaftaran}, catatan={catatan}")

            peserta.StatusPendaftaran.status_berkas = status_berkas
            peserta.StatusPendaftaran.status_daftar = status_pendaftaran

            # Simpan catatan jika status berkas adalah Revisi
            if status_berkas == 'Revisi':
                peserta.StatusPendaftaran.catatan = catatan
            else:
                peserta.StatusPendaftaran.catatan = None

            db.session.commit()
            flash('Status berhasil diperbarui.', 'success')
            logger.debug("Status pendaftaran berhasil diperbarui.")
            return redirect(url_for('datapendaftaran'))

        except Exception as e:
            db.session.rollback()
            logger.error(f"Terjadi kesalahan saat memperbarui status: {e}")
            flash(f"Terjadi kesalahan saat memperbarui data: {e}", 'danger')

    return render_template('detail-datapeserta-kelberkas.html', peserta=peserta)


@app.route('/datapesertaprakerin')
def datapesertaprakerin():
    try:
        # Query data peserta yang statusnya diterima
        data_peserta = (
            db.session.query(
                DataPeserta.id,
                DataPeserta.nama,
                User.email,
                DataPeserta.asal_kampus,
                DataPeserta.tanggal_dimulai,
                DataPeserta.tanggal_berakhir,
                StatusPendaftaran.nama_divisi
            )
            .join(User, DataPeserta.id_user == User.id)
            .join(StatusPendaftaran, DataPeserta.id == StatusPendaftaran.id_peserta)
            .filter(StatusPendaftaran.status_daftar == 'Diterima')
            .all()
        )
        # Tambahkan log untuk memeriksa hasil query
        print(f"Jumlah peserta diterima: {len(data_peserta)}")

        return render_template('datapesertaprakerin.html', data_peserta=data_peserta)
    
    except Exception as e:
        import traceback
        print("Error saat memproses data peserta prakerin:")
        print(traceback.format_exc())
        flash(f"Terjadi kesalahan: {e}", "danger")
        return redirect(url_for('homeadmin'))

from flask import request, send_file, flash, redirect, url_for
from fpdf import FPDF
from io import BytesIO
from datetime import datetime

@app.route('/generate_report', methods=['POST'])
def generate_report():
    try:
        # Mengambil filter dari form
        tanggal_mulai = request.form.get('tanggal_mulai')
        tanggal_selesai = request.form.get('tanggal_selesai')
        asal_kampus = request.form.get('asal_kampus')
        nama_divisi = request.form.get('nama_divisi')

        # Debug log filter yang diterima
        print(f"Filter diterima - Tanggal Mulai: {tanggal_mulai}, Tanggal Selesai: {tanggal_selesai}, "
              f"Asal Kampus: {asal_kampus}, Nama Divisi: {nama_divisi}")

        # Query data peserta berdasarkan filter
        query = db.session.query(
            DataPeserta.nama,
            DataPeserta.asal_kampus,
            DataPeserta.tanggal_dimulai,
            DataPeserta.tanggal_berakhir,
            StatusPendaftaran.nama_divisi
        ).join(StatusPendaftaran, DataPeserta.id == StatusPendaftaran.id_peserta)

        if tanggal_mulai and tanggal_selesai:
            query = query.filter(
                DataPeserta.tanggal_dimulai >= datetime.strptime(tanggal_mulai, '%Y-%m-%d'),
                DataPeserta.tanggal_berakhir <= datetime.strptime(tanggal_selesai, '%Y-%m-%d')
            )
        if asal_kampus:
            query = query.filter(DataPeserta.asal_kampus.ilike(f"%{asal_kampus}%"))
        if nama_divisi:
            query = query.filter(StatusPendaftaran.nama_divisi.ilike(f"%{nama_divisi}%"))

        data_peserta = query.all()
        print(f"Jumlah data peserta yang ditemukan: {len(data_peserta)}")

        if not data_peserta:
            flash('Tidak ada data yang sesuai dengan filter.', 'warning')
            return redirect(url_for('datapesertaprakerin'))
        
        # Membuat dokumen PDF menggunakan FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        # Menambahkan margin halaman
        pdf.set_left_margin(10)
        pdf.set_right_margin(15)
        
        # Menambahkan logo
        pdf.image('static/images/logopindad.png', 10, 8, 33)
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'PT PINDAD', ln=True, align='C')
        pdf.cell(0, 10, 'Laporan Data Peserta Prakerin', ln=True, align='C')
        pdf.ln(10)

        # Menambahkan header tabel
        pdf.set_font('Times', 'B', 10)
        column_widths = [10, 40, 50, 25, 25, 40]  # Lebar kolom yang disesuaikan
        headers = ['No', 'Nama', 'Asal Kampus', 'Tanggal Dimulai', 'Tanggal Berakhir', 'Divisi']

        # Menulis header tabel
        for i, header in enumerate(headers):
            pdf.cell(column_widths[i], 10, header, 1, 0, 'C')
        pdf.ln()        

        # Menambahkan data peserta ke tabel
        pdf.set_font('Times', '', 10)
        for i, peserta in enumerate(data_peserta, 1):
            pdf.cell(column_widths[0], 10, str(i), 1, 0, 'C')
            pdf.cell(column_widths[1], 10, peserta.nama, 1, 0, 'L')
            pdf.cell(column_widths[2], 10, peserta.asal_kampus, 1, 0, 'L')
            pdf.cell(column_widths[3], 10, peserta.tanggal_dimulai.strftime('%d/%m/%Y'), 1, 0, 'C')
            pdf.cell(column_widths[4], 10, peserta.tanggal_berakhir.strftime('%d/%m/%Y'), 1, 0, 'C')
            pdf.cell(column_widths[5], 10, peserta.nama_divisi, 1, 1, 'L')

        # Menambahkan tanggal dan waktu pembuatan di bawah halaman
        pdf.ln(10)
        pdf.set_font('Times', 'I', 9)
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        user_name = session.get('user_name', 'Unknown User')
        pdf.cell(0, 10, f'Dibuat pada: {timestamp} oleh {user_name}', 0, 0, 'R')
       
        # Menyimpan file ke buffer
        output = BytesIO()
        output.write(pdf.output(dest='S').encode('latin1'))
        output.seek(0)

        # Mengirimkan file ke pengguna
        return send_file(output, as_attachment=True, download_name='Laporan_Peserta_Prakerin.pdf', mimetype='application/pdf')

    except Exception as e:
        import traceback
        print("Error saat membuat laporan:")
        print(traceback.format_exc())        
        flash(f"Terjadi kesalahan saat membuat laporan: {str(e)}", 'danger')
        return redirect(url_for('datapesertaprakerin'))


@app.route('/detailpesertaprakerin/<int:id>')
def detailpesertaprakerin(id):
    try:
        # Query untuk mengambil detail peserta berdasarkan ID
        peserta = (
            db.session.query(DataPeserta, User, StatusPendaftaran, BerkasPeserta)
            .join(User, DataPeserta.id_user == User.id)
            .join(StatusPendaftaran, DataPeserta.id == StatusPendaftaran.id_peserta)
            .join(BerkasPeserta, DataPeserta.id == BerkasPeserta.id_peserta)
            .filter(DataPeserta.id == id)
            .first()
        )

        if not peserta:
            flash('Data peserta tidak ditemukan.', 'warning')
            return redirect(url_for('datapesertaprakerin'))

        return render_template('detailpesertaprakerin.html', peserta=peserta)

    except Exception as e:
        import traceback
        print("Error saat memproses detail peserta prakerin:")
        print(traceback.format_exc())
        flash(f"Terjadi kesalahan: {e}", "danger")
        return redirect(url_for('datapesertaprakerin'))


@app.route('/datawawancara', methods=['GET', 'POST'])
def datawawancara():
    try:
        peserta_wawancara = db.session.query(
            DataPeserta.id,
            DataPeserta.nama,
            User.email,
            DataPeserta.asal_kampus,
            StatusPendaftaran.tanggal_wawancara
        ).join(User, DataPeserta.id_user == User.id)\
         .join(StatusPendaftaran, DataPeserta.id == StatusPendaftaran.id_peserta)\
         .filter(StatusPendaftaran.status_daftar == 'Wawancara')\
         .all()

        if request.method == 'POST':
            # Proses input tanggal wawancara
            peserta_ids = request.form.getlist('peserta_ids')
            tanggal_wawancara = request.form.getlist('tanggal_wawancara')
            selesai_wawancara = request.form.getlist('selesai_wawancara')

            for i, peserta_id in enumerate(peserta_ids):
                peserta = StatusPendaftaran.query.filter_by(id_peserta=peserta_id).first()
                # peserta.tanggal_wawancara = tanggal_wawancara[i]
                peserta.tanggal_wawancara = datetime.strptime(tanggal_wawancara[i], '%Y-%m-%dT%H:%M')
                # Update status menjadi 'Diterima' jika selesai wawancara dicentang
                if str(peserta_id) in selesai_wawancara:
                    peserta.status_daftar = 'Diterima'
            
            db.session.commit()
            flash('Tanggal wawancara berhasil ditentukan.', 'success')
            return redirect(url_for('datawawancara'))

        return render_template('datapeserta-wawancara.html', peserta_wawancara=peserta_wawancara)
    except Exception as e:
        flash(f'Terjadi kesalahan: {e}', 'danger')
        return redirect(url_for('homeadmin'))

@app.route('/selesaikanwawancara/<int:id>', methods=['POST'])
def selesaikanwawancara(id):
    try:
        peserta = StatusPendaftaran.query.filter_by(id_peserta=id).first()
        peserta.status_daftar = 'Diterima'
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)})


# Route halaman logout
@app.route('/logout')
def logout():
    session.clear()
    flash('Anda telah logout.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5002)
