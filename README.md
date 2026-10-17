
# Pertemuan 07 - Fungsi Python

**Nama:** Azizah Nur Kholishah

**NIM:** 2225250116

**Kelas:** 3E

## Tujuan

Menggunakan fungsi, parameter, `return value`, dan scope untuk membuat program Python yang modular. Praktik ini juga menerapkan fungsi pada beberapa perhitungan matematika sederhana sehingga kode lebih terstruktur, mudah dibaca, diuji, dan digunakan kembali.

## Cara Menjalankan

**Melalui IDLE atau Python:** Buka berkas `praktik/utilitas_matematika.py`, lalu jalankan program. Pilih operasi matematika melalui menu yang ditampilkan dan masukkan angka sesuai permintaan program.

**Melalui terminal (Python 3):** Jalankan perintah berikut dari folder utama proyek:

```bash
python3 praktik/utilitas_matematika.py
```

Jika menggunakan Windows dan perintah `python3` tidak bisa digunakan, jalankan perintah berikut:

```bash
python praktik/utilitas_matematika.py
```

Untuk mencoba latihan, buka masing-masing berkas pada folder `latihan/` dan jalankan secara terpisah sesuai instruksi pada program.

## Struktur Fungsi

Program `utilitas_matematika.py` terdiri atas beberapa fungsi yang memiliki tugas berbeda. Berikut penjelasannya.

| No. | Nama Fungsi | Parameter | Kegunaan | Proses Perhitungan |
|---|---|---|---|---|
| 1 | `luas_persegi_panjang(p, l)` | `p` = panjang, `l` = lebar | Menghitung luas persegi panjang. | Mengalikan panjang dengan lebar (`p * l`). |
| 2 | `luas_segitiga(a, t)` | `a` = alas, `t` = tinggi | Menghitung luas segitiga. | Mengalikan alas dengan tinggi, kemudian membaginya dengan 2 (`0.5 * a * t`). |
| 3 | `jumlah_n(n)` | `n` = batas bilangan | Menghitung jumlah bilangan dari 1 sampai n. | Menjumlahkan bilangan menggunakan perulangan. |
| 4 | `faktorial(n)` | `n` = bilangan yang dihitung faktorialnya | Menghitung nilai faktorial suatu bilangan. | Mengalikan bilangan dari 1 sampai n menggunakan perulangan. |
| 5 | `tampilkan_menu()` | Tidak ada parameter | Menampilkan pilihan operasi matematika kepada pengguna. | Menampilkan daftar menu menggunakan `print()`. |

## Hasil Pengujian

| Operasi | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| Luas persegi panjang | p = 8, l = 5 | 40 | 40 | Berhasil |
| Luas segitiga | a = 10, t = 6 | 30.0 | 30.0 | Berhasil |
| Jumlah 1 sampai n | n = 10 | 55 | 55 | Berhasil |
| Faktorial | n = 5 | 120 | 120 | Berhasil |
| Faktorial | n = 0 | 1 | 1 | Berhasil |

## Refleksi

Setelah mempelajari fungsi Python, saya memahami bahwa program dapat dibagi menjadi beberapa bagian sesuai tugasnya. Dengan menggunakan fungsi, rumus tidak perlu ditulis berulang kali dan program menjadi lebih mudah dibaca. Saya juga memahami perbedaan `print()` dan `return`, penggunaan parameter, serta pentingnya variabel lokal agar tidak terjadi kesalahan saat program dijalankan.

## Exit Ticket

1. **Satu alasan utama menggunakan fungsi:** Agar kode program lebih terstruktur, tidak perlu ditulis berulang kali, dan dapat digunakan kembali.
2. **Satu kesalahan yang saya temukan terkait parameter atau return:** Memahami perbedaan print() dan return. Setelah mempelajarinya, saya memahami bahwa print() digunakan untuk menampilkan hasil ke layar, sedangkan return digunakan untuk mengembalikan nilai agar dapat digunakan kembali dalam perhitungan lain.
3. **Materi Pertemuan 1-7 yang perlu saya ulang untuk persiapan UTS:** nested loop, fungsi, parameter, return, dan scope. 