## 🕵️ SPY-E PERSONA-SCRAPER v1.0

![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Windows-red?style=for-the-badge&logo=android)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Unit](https://img.shields.io/badge/Unit-123Tool%20Intelligence-7000ff?style=for-the-badge)

**Persona-Scraper** adalah alat investigasi **OSINT (Open Source Intelligence)** tingkat lanjut yang dirancang untuk melacak jejak digital target berdasarkan username. Alat ini bekerja secara asinkron untuk menyisir ratusan platform dan basis data kebocoran dalam hitungan detik.

---

## ⚡ Fitur Utama
- **Multi-Platform Search:** Mencari akun aktif di Instagram, GitHub, TikTok, Telegram, dan 100+ situs lainnya.
- **Data Breach Intelligence:** Terintegrasi dengan database kebocoran data untuk melihat status kerentanan target.
- **Image Metadata Audit (EXIF):** Mengunduh foto profil secara otomatis dan membedah data tersembunyi (Kamera, Lokasi, Perangkat).
- **Asynchronous Engine:** Kecepatan tinggi menggunakan `aiohttp` tanpa membebani sistem.
- **Auto-Logging:** Semua hasil audit gambar disimpan otomatis di folder `intel_reports/`.

---

## 🛠️ Instalasi & Persiapan

### 1. Prasyarat
Pastikan Anda sudah menginstal **Python 3.x** di perangkat Anda (PC/Laptop atau Termux).

### 2. Clone Repositori
```bash
git clone [https://github.com/username-kamu/persona-scraper.git](https://github.com/username-kamu/persona-scraper.git)
cd persona-scraper
