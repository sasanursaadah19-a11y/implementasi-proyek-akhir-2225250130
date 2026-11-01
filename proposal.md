# PROPOSAL PROYEK
## Program Rekap dan Analisis Nilai Matematika Siswa

### 1. Latar Belakang

Pengolahan nilai siswa merupakan salah satu kegiatan yang dilakukan oleh guru dalam proses pembelajaran. Pengolahan nilai secara manual membutuhkan waktu dan berpotensi menimbulkan kesalahan dalam perhitungan. Oleh karena itu, diperlukan program sederhana yang dapat membantu proses pengolahan nilai secara lebih cepat dan terstruktur.

Program ini dibuat menggunakan bahasa Python untuk membantu melakukan pencatatan nilai, menghitung statistik nilai, menentukan status ketuntasan, serta menyimpan data hasil pengolahan.

### 2. Pengguna dan Tujuan Program

**Pengguna:** Guru matematika.

**Tujuan:**
- Mempermudah pencatatan nilai siswa.
- Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
- Menentukan status ketuntasan siswa berdasarkan KKM.
- Menyimpan data dan hasil pengolahan nilai.

### 3. Ruang Lingkup Proyek

Fitur utama program:
1. Memasukkan nama dan nilai siswa.
2. Menampilkan data nilai siswa.
3. Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
4. Menentukan status lulus atau tidak lulus berdasarkan KKM.
5. Menyimpan data ke dalam file.

**Batasan proyek:**
- Program menggunakan bahasa Python.
- Program dijalankan melalui terminal atau console.
- Nilai siswa berada pada rentang 0–100.
- KKM yang digunakan adalah 75.
- Program tidak menggunakan database maupun antarmuka grafis.

### 4. Kebutuhan Program

**Kebutuhan fungsional:**
- Program dapat menerima nama dan nilai siswa.
- Program dapat memvalidasi nilai pada rentang 0–100.
- Program dapat menampilkan data siswa.
- Program dapat menghitung statistik nilai.
- Program dapat menentukan status ketuntasan.
- Program dapat menyimpan data ke file.

**Kebutuhan nonfungsional:**
- Program mudah dijalankan melalui terminal VS Code.
- Pesan kesalahan mudah dipahami.
- Nama variabel dan fungsi mudah dimengerti.
- Program dapat diuji menggunakan data contoh.

### 5. Input, Proses, dan Output (IPO)

| Input | Proses | Output |
|---|---|---|
| Nama dan nilai siswa | Validasi data | Data siswa |
| Data nilai | Menghitung rata-rata | Rata-rata nilai |
| Data nilai | Mencari nilai tertinggi dan terendah | Nilai tertinggi dan terendah |
| Nilai dan KKM | Menentukan status ketuntasan | Status lulus atau tidak lulus |
| Seluruh data | Menyimpan data ke file | File rekap nilai |

### 6. Algoritma dan Pseudocode

```text
MULAI
    Siapkan tempat penyimpanan data siswa
    Tentukan KKM = 75

    Masukkan nama dan nilai siswa
    Periksa validitas nilai

    Jika nilai tidak berada pada rentang 0–100:
        Tampilkan pesan kesalahan
    Jika valid:
        Simpan data siswa

    Tampilkan seluruh data siswa

    Jika data tersedia:
        Hitung rata-rata nilai
        Cari nilai tertinggi
        Cari nilai terendah
        Tentukan status ketuntasan
        Tampilkan hasil pengolahan
        Simpan data ke file
    Jika data kosong:
        Tampilkan pesan bahwa data belum tersedia

SELESAI
```

### 7. Struktur Program

Program dirancang menggunakan beberapa file dengan tanggung jawab berbeda.

| File | Fungsi |
|---|---|
| `main.py` | Mengatur jalannya program |
| `input_data.py` | Mengelola input dan validasi data |
| `proses.py` | Menghitung statistik dan status ketuntasan |
| `output.py` | Menampilkan dan menyimpan hasil |

### 8. Struktur Data

Struktur data yang digunakan:
- **List:** Menampung kumpulan data siswa.
- **Dictionary:** Menyimpan informasi setiap siswa, seperti nama dan nilai.
- **Variabel:** Menyimpan nilai KKM, rata-rata, nilai tertinggi, dan nilai terendah.
- **File:** Menyimpan data hasil pengolahan.

### 9. Test Case

| ID | Kondisi Pengujian | Input | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Nilai valid | Nilai 85 | Data berhasil disimpan |
| TC02 | Nilai sama dengan KKM | Nilai 75 | Status Lulus |
| TC03 | Nilai di bawah KKM | Nilai 60 | Status Tidak Lulus |
| TC04 | Nilai melebihi batas | Nilai 110 | Muncul pesan kesalahan |
| TC05 | Data kosong | Belum ada data siswa | Muncul pesan data belum tersedia |
| TC06 | Perhitungan rata-rata | 80, 70, 90 | Rata-rata 80 |
| TC07 | Penyimpanan data | Nama Ani, nilai 85 | Data tersimpan dalam file |

### 10. Pembagian Tugas

Proyek dikerjakan secara individu oleh Sasa Nursaadah.

| Kegiatan | Penanggung Jawab |
|---|---|
| Perancangan proyek | Sasa Nursaadah |
| Pembuatan struktur program | Sasa Nursaadah |
| Pengelolaan input dan validasi | Sasa Nursaadah |
| Pengolahan dan analisis nilai | Sasa Nursaadah |
| Pengujian program | Sasa Nursaadah |
| Dokumentasi dan GitHub | Sasa Nursaadah |

### 11. Jadwal Pengerjaan

| Tahapan | Target |
|---|---|
| Pertemuan 14 | Perancangan proposal dan persiapan repository |
| Pertemuan 15 | Implementasi, pengujian, dan debugging |
| Pertemuan 16 | Presentasi dan demonstrasi proyek |

### 12. Repository GitHub

Repository proyek:

https://github.com/sasanursaadah19-a11y/proyek-akhir-2225250130

Branch utama yang digunakan adalah `main`.