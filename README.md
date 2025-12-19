# Student Registration Validation System (SOLID)

##  Deskripsi Proyek
Proyek ini merupakan contoh sederhana **Sistem Validasi Registrasi Mahasiswa** yang telah direfaktor dengan menerapkan prinsip **SOLID**, khususnya:
- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)
- Dependency Inversion Principle (DIP)

Proyek ini dibuat sebagai bagian dari tugas mata kuliah **Pemrograman Berorientasi Objek (PBO)**.

---

##  Studi Kasus
Sistem melakukan validasi registrasi mahasiswa berdasarkan:
- Jumlah SKS
- Status prasyarat
- IPK mahasiswa

Validasi dilakukan menggunakan **Dependency Injection**, sehingga aturan validasi dapat ditambahkan tanpa mengubah kode utama.

---

##  Struktur Kode
- `Validator` → Interface (abstraksi aturan validasi)
- `SKSValidator` → Validasi batas SKS
- `PrasyaratValidator` → Validasi prasyarat mata kuliah
- `IPKValidator` → Validasi IPK (challenge OCP)
- `ValidatorManager` → Mengelola proses validasi (SRP)
- Logging digunakan untuk mencatat hasil validasi

---

## ▶ Cara Menjalankan Program
1. Pastikan Python sudah terinstal
2. Jalankan perintah berikut di terminal:
   ```bash
   python registration.py
