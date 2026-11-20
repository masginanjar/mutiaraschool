# Mutiara School Bali — mutiaraschool.com

Website statis 2 bahasa (Inggris di `/`, Indonesia di `/id/`).

- `public_html/` — hasil jadi yang ditayangkan (GitHub Pages).
- `tools/content.py`, `tools/pages.py` — semua teks; `tools/build.py` membangun ulang `public_html/`; `tools/check.py` pengecekan.
- `src/assets/` — CSS, JS, foto sumber.

Mengubah isi: edit file di `tools/` atau `src/`, lalu `python3 tools/build.py && python3 tools/check.py`, commit, push ke `main`.
