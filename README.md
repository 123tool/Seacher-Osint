## 🕵️ SEARCHER OSINT SCRAPER

Alat investigasi **OSINT (Open Source Intelligence)** tingkat lanjut yang dirancang untuk melacak jejak digital target berdasarkan username. Alat ini bekerja secara asinkron untuk menyisir ratusan platform dan basis data kebocoran dalam hitungan detik.

---

## ⚡ Fitur Utama
- **Multi-Platform Search:** Mencari akun aktif di Instagram, GitHub, TikTok, Telegram, dan 100+ situs lainnya.
- **Data Breach Intelligence:** Terintegrasi dengan database kebocoran data untuk melihat status kerentanan target.
- **Image Metadata Audit (EXIF):** Mengunduh foto profil secara otomatis dan membedah data tersembunyi (Kamera, Lokasi, Perangkat).
- **Asynchronous Engine:** Kecepatan tinggi menggunakan `aiohttp` tanpa membebani sistem.
- **Auto-Logging:** Semua hasil audit gambar disimpan otomatis di folder `intel_reports/`.

---

## 🛠️ Instalasi & Persiapan

## 1. Prasyarat
Pastikan Anda sudah menginstal **Python 3.x** di perangkat Anda (PC/Laptop atau Termux).

## 2. Install Dependensi
​Jalankan perintah ini untuk menginstal semua library pendukung :
```
pip install aiohttp colorama prettytable pillow
```
## 3. Clone Repositori
```bash
git clone [https://github.com/123tool/Seacher-Osint.git](https://github.com/123tool/Seacher-Osint.git)
cd Seacher-Osint
```

## 4. Panduan Penggunaan
​Gunakan perintah dasar diikuti dengan username target yang ingin diinvestigasi :
```
python main.py [username_target]
```
Contoh :
```
python main.py agus_setiadi
```
## Struktur Output
​Setiap kali investigasi berhasil menangkap gambar profil target, file akan disimpan dengan struktur :
```
​intel_reports/[username]_avatar.jpg -> Foto profil yang diambil.
​Terminal Output -> Tabel lengkap berisi URL aktif dan status keamanan data.
```
## Logika Operasional :

​**Script ini menggunakan logika Status Code
Analysis. Jika target ditemukan (HTTP 200), sistem akan langsung mengunci URL tersebut sebagai bukti fisik. Jika target pernah masuk dalam database kebocoran, label VULNERABLE akan muncul sebagai peringatan merah.**

​⚠️ Disclaimer

​**Alat ini dibuat oleh 123TOOL hanya untuk tujuan Edukasi, Forensik Digital, dan Keamanan Jaringan. Penggunaan alat ini untuk tindakan penguntitan (stalking) atau ilegal adalah tanggung jawab pengguna sepenuhnya.**
