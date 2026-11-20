# Mutiara School – website statis 2 bahasa (mutiaraschool.com)

Bahasa default Inggris di `/`, Indonesia di `/id/`.
7 halaman per bahasa: Beranda, Tentang Kami, Program, Fasilitas, Galeri, Pendaftaran, Kontak.

## Struktur folder
```
public_html/                 <- ISI folder ini yang di-upload ke cPanel
├── index.html               Home (Inggris)
├── about/ programmes/ facilities/ gallery/ admissions/ contact/   (masing-masing berisi index.html)
├── id/index.html            Beranda (Indonesia)
├── id/tentang-kami/ program/ fasilitas/ galeri/ pendaftaran/ kontak/
├── assets/css/style.css  assets/js/main.js  assets/img/ (favicon)
├── favicon.ico  sitemap.xml  robots.txt  404.html  .htaccess
src/assets/                  sumber CSS & JS
tools/content.py             teks beranda, kontak, daftar URL foto
tools/pages.py               teks 6 halaman lain
tools/build.py               membuat ulang public_html
tools/check.py               pengecekan: gagal kalau ada kata terlarang / link rusak / alt kosong
```

## Cara upload ke cPanel
1. Login cPanel hosting mutiaraschool.com, buka **File Manager**.
2. Di pojok kanan atas klik **Settings**, centang **Show Hidden Files** (supaya file `.htaccess` terlihat).
3. Masuk ke folder **public_html**. Kalau ada file lama, backup dulu lalu hapus.
4. Klik **Upload**, pilih `mutiaraschool-public_html.zip`.
5. Klik kanan zip itu → **Extract** → tujuan `/public_html`, lalu hapus file zip.
6. Pastikan `index.html`, folder `id`, `about`, `assets`, dst. berada LANGSUNG di dalam public_html.
7. Aktifkan SSL di cPanel → SSL/TLS Status, lalu buka https://mutiaraschool.com/ dan /id/.
8. Opsional: daftarkan https://mutiaraschool.com/sitemap.xml di Google Search Console.

## Kalau mengubah teks
Edit `tools/content.py` atau `tools/pages.py`, lalu jalankan:
```
python3 tools/build.py && python3 tools/check.py
```
Upload ulang hanya kalau check.py menampilkan "LULUS".

## Catatan
- Foto dan lambang sekolah sekarang disimpan di dalam situs (`assets/img/foto/` dan `assets/img/crest.webp`, format WebP dua ukuran supaya ringan), jadi tidak bergantung pada website lama. Foto diambil dari tampilan layar website lama dengan lebar sekitar 800 px (foto utama 1600 px).
- Font diambil dari Google Fonts (Manrope).
- `.htaccess` berisi halaman 404, kompresi, dan cache browser.
