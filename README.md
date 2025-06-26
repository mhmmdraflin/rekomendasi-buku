# 📚 Sistem Rekomendasi Buku & CRUD Web App

Aplikasi ini adalah sistem rekomendasi buku interaktif berbasis web yang dibangun menggunakan Python Flask & MySQL. Aplikasi ini memungkinkan pengguna untuk:

* Memilih minat (Teknologi, Fiksi, Sejarah)
* Melihat daftar buku sesuai minat dengan gambar, penulis, dan tahun terbit
* Mengelola database buku (tambah, edit, hapus)

---

## 🎯 Fitur Utama

* ✅ Form pilihan minat pengguna
* ✅ Menampilkan hasil rekomendasi dalam bentuk kartu (card) Bootstrap
* ✅ Menampilkan gambar, author, dan tahun terbit
* ✅ Menambahkan buku baru ke database
* ✅ Mengedit data buku yang ada
* ✅ Menghapus buku
* ✅ Tampilan rapi dengan Bootstrap 5
---

## 🛠 Teknologi yang Digunakan

| Teknologi    | Keterangan                    |
| ------------ | ----------------------------- |
| Python       | Bahasa backend                |
| Flask        | Web Framework untuk Python    |
| MySQL        | Database relasional           |
| Bootstrap 5  | Styling modern dan responsif  |
| HTML5 + CSS3 | Struktur dan tampilan halaman |

---

## ⚙️ Cara Menjalankan Aplikasi

1. Pastikan Python & pip sudah terinstall
2. Install dependency:

   ```
   pip install flask mysql-connector-python
   ```
3. Import file db\_rekomendasi.sql ke MySQL (via phpMyAdmin)
4. Jalankan aplikasi:

   ```
   python server.py
   ```
5. Akses aplikasi melalui browser:
   [http://localhost:5000](http://localhost:5000)

---

## 🗃️ Struktur Folder

```
📁 proyek/
├── server.py                # file utama aplikasi Flask
├── db_rekomendasi.sql       # file struktur database MySQL
└── web/
    └── index.html           # (opsional) file HTML statis awal
```

---

## 💾 Penyimpanan Data

* Data buku disimpan di database MySQL (lokal) dalam tabel buku
* Field: judul, minat, image\_url, author, tahun\_terbit

---

## 👨‍👩‍👧‍👦 Kelompok - Paradigma Deklaratif

| Nama                     | NIM       |
| ------------------------ | --------- |
| Muhammad Rafli Nurfathan | 221111009 |
| Gilbert Jeremy Nathanael | 221111028 |
| Marcello Ilham           | 221111029 |
| Danang Arya Pratama      | 231111024 |

---

📄 Lisensi: Open Source — Bebas digunakan dan dimodifikasi untuk pembelajaran.

—
