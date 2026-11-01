# Test Case
## Program Rekap dan Analisis Nilai Matematika Siswa

Pengujian dilakukan untuk memastikan setiap fitur program berjalan sesuai dengan hasil yang diharapkan.

| ID | Kondisi Pengujian | Input | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Memasukkan nilai valid | Nilai 85 | Data siswa berhasil disimpan |
| TC02 | Nilai sama dengan KKM | Nilai 75 | Status siswa Lulus |
| TC03 | Nilai di bawah KKM | Nilai 60 | Status siswa Tidak Lulus |
| TC04 | Nilai melebihi batas | Nilai 110 | Program menampilkan pesan kesalahan |
| TC05 | Data siswa kosong | Tidak ada data siswa | Program menampilkan pesan data belum tersedia |
| TC06 | Menghitung rata-rata | 80, 70, 90 | Rata-rata nilai adalah 80 |
| TC07 | Menyimpan data siswa | Nama Ani, nilai 85 | Data siswa berhasil disimpan ke dalam file |

## Kesimpulan Pengujian

Ketujuh test case tersebut digunakan sebagai acuan untuk menguji validasi input, pengolahan nilai, penentuan ketuntasan, dan penyimpanan data. Hasil aktual akan dicatat setelah program selesai diimplementasikan dan diuji.