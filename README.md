<p align="center">
  <img src="sticker.png" alt="ChatGPT K-12 Banner" width="400" />
</p>

# ChatGPT K-12 Teachers Verification Tool

Tools Python canggih yang dirancang untuk **keperluan edukasi dan riset** dalam mengotomatisasi proses verifikasi guru K-12 dengan SheerID. Tools ini mendukung berbagai platform dan menyediakan metode koneksi fleksibel.

## ⚡ Instalasi Cepat

### Untuk Pengguna Windows (Direkomendasikan)

1. **Download Tools**
   - Download versi terbaru dari bagian Releases
   - Extract file ZIP ke lokasi pilihan Anda

2. **Dapatkan URL Verifikasi**
   - Login ke [https://chatgpt.com/](https://chatgpt.com/)
   - Buka [https://chatgpt.com/k12-verification](https://chatgpt.com/k12-verification)
   - Salin URL verifikasi SheerID dari layanan tersebut

3. **Jalankan Tools**
   - **Windows 32-bit**: Gunakan folder `PyRuntime_32`
   - **Windows 64-bit**: Gunakan folder `PyRuntime_64`
   - Double klik `run_cmd.bat`
   - Tempel URL verifikasi saat diminta

## 🖥️ Pengguna Windows

### Langkah Detail untuk Windows:

1. **Download Package:**
   ```
   ChatGPT-K-12-Teachers-Verification-Tool.zip
   ```

2. **Extract ke folder:**
   ```bash
   C:\ChatGPT_K12_Tool\
   ```

3. **Tentukan versi Windows:**
   - Buka **Settings** → **System** → **About**
   - Lihat **System type**:
     - **64-bit operating system** → Gunakan folder `PyRuntime_64`
     - **32-bit operating system** → Gunakan folder `PyRuntime_32`

4. **Jalankan Tools:**
   ```
   Double klik: run_cmd.bat
   ```

5. **Masukkan URL:**
   ```bash
   ============================================
        PYTHON SCRIPT LAUNCHER (INTERACTIVE)
   ============================================

   Masukkan URL Services SheerID: https://services.sheerid.com/verify/xxxabc123?verificationId=xxx123abc
   ```

6. **Pilih Mode Koneksi:**
   ```bash
   Pilih Metode Koneksi:
   [1]  Direct dengan email temporary (default)
   [2]  Dengan proxy (ip:port)
   [3]  Dengan proxy auth (user:pass)
   [4]  Debug mode (no proxy)
   [5]  Debug mode + proxy (ip:port)
   [6]  Debug mode + proxy auth (user:pass)
   [7]  Tanpa email temporary
   [8]  Tanpa email temporary + proxy (ip:port)
   [9]  Tanpa email temporary + proxy auth (user:pass)
   [10] Email Manual
   [11] Email Manual + proxy (ip:port)
   [12] Email Manual + proxy auth (user:pass)
   [13] Keluar

   Pilih nomor (1-13): 
   ```

## 📱 Pengguna Termux/Kali

```bash
# Install Termux (Android)
# Buka Termux, jalankan:

pkg update && pkg upgrade
pkg install python git
git clone https://github.com/itzluthfi/Farm-Acc-ChatGPT-K-12-Teachers-Verification-Too.git chatgpt-k12-verifier
cd chatgpt-k12-verifier/PyRuntime_32 atau cd chatgpt-k12-verifier/PyRuntime_64
pip install httpx requests Pillow cloudscraper

# Jalankan dengan CLI
python script.py "URL_VERIFIKASI" [OPTIONS]
```

### Untuk Kali Linux:
```bash
sudo apt update
sudo apt install python3 python3-pip git
git clone https://github.com/itzluthfi/Farm-Acc-ChatGPT-K-12-Teachers-Verification-Too.git chatgpt-k12-verifier
cd chatgpt-k12-verifier/PyRuntime_32 atau cd chatgpt-k12-verifier/PyRuntime_64
pip3 install httpx requests Pillow cloudscraper
```

## 🔧 Metode Instalasi

### Metode 1: Windows Executable (Paling Mudah)
1. Download file executable dari Releases
2. Extract dan jalankan `run_cmd.bat`
3. **Tidak perlu install Python**

### Metode 2: Manual Python Installation (Optional hanya jika ada Error Modul)
```bash
# Install package yang diperlukan
pip install httpx requests Pillow cloudscraper

# Atau gunakan requirements.txt
pip install -r requirements.txt
```

### Metode 3: Docker (Advanced)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install httpx requests Pillow cloudscraper
CMD ["python", "script.py"]
```

## 🚀 Contoh Penggunaan

### Penggunaan Dasar (Default)
```bash
python script.py "https://services.sheerid.com/verify/xxxabc123?verificationId=xxx123abc"
```

### Dengan Proxy
```bash
# Proxy sederhana
python script.py "URL" --proxy "127.0.0.1:8080"

# Proxy dengan autentikasi
python script.py "URL" --proxy "user:password@127.0.0.1:8080"
```

### Debug Mode
```bash
python script.py "URL" --debug
```

### Input Email Manual
```bash
# Via argument
python script.py "URL" --email "user@example.com"

# Prompt interaktif
python script.py "URL" --ask-email
```

### Tanpa Email Temporary
```bash
python script.py "URL" --no-temp-email
```

## 📊 Metode Koneksi

| No | Metode | Deskripsi | Cocok Untuk |
|----|--------|-----------|-------------|
| 1 | **Direct dengan temp email** | Koneksi langsung + email temporary | Testing cepat, tanpa proxy |
| 2-3 | **Dengan Proxy** | Lewat proxy server | Bypass restriksi |
| 4-6 | **Debug Mode** | Output verbose | Troubleshooting & development |
| 7-9 | **Tanpa temp email** | Email generated tanpa service temp | Hindari blok email temporary |
| 10-12| **Email Manual** | Pakai email sendiri | Butuh klik link verifikasi |

## 🎯 Fitur Utama

- ✅ **Multi-Platform**: Windows (optimized), Termux, Kali Linux
- ✅ **Berbagai Metode Koneksi**: Direct, Proxy, Debug modes
- ✅ **Opsi Email**: Temporary, Manual, atau Generated emails
- ✅ **Auto-Click Verification**: Otomatis klik link verifikasi
- ✅ **Database Sekolah K-12 Asli**: Pakai ID sekolah valid dari SheerID
- ✅ **Generasi Dokumen Profesional**: Buat ID card guru realistis
- ✅ **Error Handling**: Pesan error lengkap dan recovery
- ✅ **Dukungan Proxy**: HTTP/HTTPS proxy dengan autentikasi
- ✅ **User-Friendly Interface**: Menu interaktif untuk Windows

## 📈 Contoh Output

### Verifikasi Berhasil
```bash
=============================================
     PYTHON SCRIPT LAUNCHER (INTERACTIVE)
=============================================

Masukkan URL Services SheerID: https://services.sheerid.com/verify/68d47554aa292d20b9bec8f7/?verificationId=abc123xyz

Pilih nomor (1-13): 1

[INFO] Memproses URL...
[INFO] Menggunakan temporary email service (otomatis klik link)
   Guru: Oliver Johnson
   Email: oliver.johnson123@sharklasers.com
   Sekolah: Thomas Jefferson High School For Science And Technology
   Tanggal lahir: 1985-03-15

   -> Langkah 1/4: Membuat kartu identitas guru...
      Ukuran dokumen: 45.23 KB
   -> Langkah 2/4: Mengirim informasi guru...
      Langkah saat ini: success

   BERHASIL! AUTO-PASS! Tidak perlu upload dokumen!

[BERHASIL] Verifikasi dikirim!
  Guru: Oliver Johnson
  Email: oliver.johnson123@sharklasers.com
  Status: AUTO-PASS (langsung disetujui)
```

### Scenario Email Loop
```bash
[EMAIL] Email verifikasi ditemukan (ID: 12345)
[EMAIL] Link ditemukan: https://services.sheerid.com/verify/68d47554aa292d20b9bec8f7/?emailToken=987654
[EMAIL] Auto-click status: 200
[EMAIL] VERIFIKASI SUKSES via auto-click!
```

### Output dengan Email Manual
```bash
[EMAIL MANUAL] PERHATIAN!
Email: user@gmail.com
Link verifikasi akan dikirim ke email Anda
Silakan cek email dan klik link verifikasi
Setelah itu, dapatkan link baru dari ChatGPT
dan jalankan script lagi dengan link baru
```

## ⚠️ Error Umum & Solusi

| Error | Penyebab | Solusi |
|-------|----------|---------|
| `URL tidak valid` | URL verifikasi salah/tidak lengkap | Cek format URL dari halaman ChatGPT K12 |
| `Proxy setup failed` | Format proxy tidak valid | Gunakan format: `ip:port` atau `user:pass@ip:port` |
| `Email loop terdeteksi` | Sekolah butuh verifikasi email | Gunakan metode [10]-[12] untuk email manual |
| `Connection timeout` | Masalah jaringan/proxy | Coba proxy berbeda atau koneksi direct |
| `Invalid school ID` | Sekolah tidak ada di database | Tools otomatis pilih sekolah valid |
| `VerificationId not found` | URL parsing gagal | Pastikan URL mengandung `verificationId=` |
| `Failed to upload to S3` | Upload dokumen gagal | Coba lagi atau ganti dokumen |

## 🔒 Keamanan & Privasi

- **Tidak Kumpulkan Data**: Tools tidak mengumpulkan atau kirim data pribadi
- **Proses Lokal**: Semua data diproses di komputer Anda
- **Email Temporary**: Pakai email sekali pakai bila memungkinkan
- **Open Source**: Kode transparan, tidak ada backdoor
- **No Logging**: Tidak ada pencatatan aktivitas pengguna

## ⚖️ Disclaimer Hukum

**TOOLS INI HANYA UNTUK TUJUAN EDUKASI DAN RISET SAJA**

- Gunakan hanya untuk testing legitimate dan scenario edukasi
- **Jangan gunakan** untuk aktivitas fraudulent atau bypass restriksi legitimate
- Hormati terms of service semua platform terkait
- Pengguna bertanggung jawab penuh atas tindakan mereka
- Developer tidak bertanggung jawab atas penyalahgunaan

## 🧪 Environment Testing

| Platform | Status | Catatan |
|----------|--------|---------|
| **Windows 10/11** | ✅ Didukung Penuh | Performa optimal |
| **Windows 7/8** | ✅ Didukung | Mungkin perlu update .NET |
| **Termux (Android)** | ⚠️ CLI Saja | Pakai command-line manual |
| **Kali Linux** | ⚠️ CLI Saja | Butuh setup Python |
| **MacOS** | ❌ Belum Diuji | Mungkin perlu penyesuaian |

## 🛠️ Detail Teknis

### Dibangun Dengan
- **Python 3.8+**: Bahasa pemrograman utama
- **httpx**: HTTP client modern untuk async requests
- **Pillow**: Image processing untuk generasi dokumen
- **Requests**: HTTP library untuk API calls
- **Cloudscraper**: Library untuk bypass Cloudflare protection

### Arsitektur
- **Desain Modular**: Komponen terpisah untuk email, verifikasi, UI
- **Error Recovery**: Penanganan gagal jaringan yang graceful
- **Dapat Dikonfigurasi**: Banyak mode untuk scenario berbeda
- **Mudah Diperluas**: Mudah tambah fitur atau sekolah baru

### Struktur File
```
ChatGPT-K-12-Teachers-Verification-Tool/
├── PyRuntime_32/                # Untuk Windows 32-bit
│   ├── script.py                # Script CLI & core verifier
│   ├── auto_k12_flow.py         # Skrip otomatisasi flow pendaftaran & verifikasi
│   ├── run_cmd.bat              # Launcher CLI interaktif
│   └── run_auto_k12.bat         # Launcher otomatisasi penuh
│
├── PyRuntime_64/                # Untuk Windows 64-bit
│   ├── script.py                # Script CLI & core verifier
│   ├── auto_k12_flow.py         # Skrip otomatisasi flow pendaftaran & verifikasi
│   ├── run_cmd.bat              # Launcher CLI interaktif
│   └── run_auto_k12.bat         # Launcher otomatisasi penuh
│
├── LICENSE                      # Lisensi MIT
└── README.md                    # Dokumentasi
```

## 🤝 Berkontribusi

Kami menerima kontribusi! Caranya:

1. Fork repository
2. Buat feature branch (`git checkout -b feature/FiturKeren`)
3. Commit changes (`git commit -m 'Tambah FiturKeren'`)
4. Push ke branch (`git push origin feature/FiturKeren`)
5. Open Pull Request

### Area untuk Kontribusi
- Tambah lebih banyak ID sekolah K-12
- Improve penanganan proxy & anti-detect browser
- Tambah metode verifikasi baru
- Optimasi performa dan dokumentasi

## ☕ Dukungan & Apresiasi

Jika tools ini bermanfaat dan menghemat waktu Anda:

### 🤫 ⚠️ Peringatan: Secret Area / Easter Egg
<details>
<summary><b>🚫 JANGAN DIKLIK! (Serius, jangan dibuka kalau nggak mau penasaran...) 🕵️‍♂️✨</b></summary>
<br>
<blockquote>
  <p><b>⚠️ PERINGATAN SISTEM:</b> Waduh, kenapa malah dibuka?! 😆<br>
  Tapi karena Anda sudah terlanjur nekat dan penasaran sampai sini... barangkali mau traktir segelas kopi lewat QRIS di bawah ini agar developer makin semangat update tools! ☕🚀</p>
</blockquote>
<br>
<p align="center">
  <img src="jangan-dibuka-kalau-ga-mau-penasaran.png" alt="Secret QRIS" width="320" />
</p>
<p align="center">
  <i>"Secangkir kopi dari Anda adalah bahan bakar baris kode berikutnya."</i> ✨<br>
  <b>Terima kasih banyak atas segala apresiasi dan dukungannya! 🙏💖</b>
</p>
</details>

<br>

### 📢 Dukung Proyek
- Beri bintang di repository ini ⭐
- Bagikan dengan rekan developer
- Laporkan issues atau saran perbaikan

## 📄 Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](LICENSE) untuk detail.

## 🙏 Ucapan Terima Kasih

- Komunitas open-source untuk libraries dan tools
- Peneliti edukasi & otomasi yang bereksplorasi secara bertanggung jawab

---

**Ingat**: Selalu gunakan tools dengan bertanggung jawab dan etis.

**Selamat Mencoba!** 🚀

---

### 📞 Kontak & Support
- **Repository**: [Farm-Acc-ChatGPT-K-12-Teachers-Verification-Too](https://github.com/itzluthfi/Farm-Acc-ChatGPT-K-12-Teachers-Verification-Too)
- **Issues**: [GitHub Issues](https://github.com/itzluthfi/Farm-Acc-ChatGPT-K-12-Teachers-Verification-Too/issues)
- **Email**: luthfishidqi2@gmail.com
- **Telegram**: [@itzluthfi](https://t.me/itzluthfi)

---
**Dikembangkan & Dipelihara oleh itzluthfi**
