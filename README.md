

## Table of Contents

1. Instalasi
2. Konfigurasi
3. Struktur Direktori
4. Penggunaan
5. Dokumentasi API
6. Kontribusi
7. Lisensi

## Instalasi

Pastikan Anda telah menginstal Python dan pip di lingkungan Anda sebelum memulai. Untuk menginstal proyek ini, ikuti langkah-langkah berikut:

1. Clone repositori ini:

   git clone <URL_REPO>
   cd nama_repo

2. Buat virtual environment (opsional, tapi disarankan):

   python -m venv venv

3. Aktifkan virtual environment (opsional):

   - Windows:

     venv\Scripts\activate

   - MacOS/Linux:

     source venv/bin/activate

4. Instal dependencies:

   pip install -r requirements.txt

## Konfigurasi

Pada file config.py, pastikan Anda telah mengkonfigurasi:

- JWT_SECRET_KEY: Kunci rahasia untuk JWT.
- Konfigurasi lain yang diperlukan untuk proyek Anda.

## Penggunaan

Penjelasan tentang cara menggunakan proyek ini:

1. Jalankan aplikasi:

   python .\app\main.py

2. Buka browser dan akses http://localhost:5000 untuk melihat hasilnya.


