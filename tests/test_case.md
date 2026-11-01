# Test Case
## Program Rekap dan Analisis Nilai Matematika Siswa

Pengujian dilakukan untuk memastikan setiap fitur program berjalan sesuai dengan hasil yang diharapkan.

| ID | Kondisi Pengujian | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| TC01 | Memasukkan nilai valid | Nama Ani, nilai 85 | Data siswa berhasil ditambahkan | Data Ani dengan nilai 85 berhasil ditambahkan | Berhasil |
| TC02 | Nilai sama dengan KKM | Nama Budi, nilai 75 | Status siswa Lulus | Budi memperoleh status Lulus | Berhasil |
| TC03 | Nilai di bawah KKM | Nama Citra, nilai 60 | Status siswa Tidak Lulus | Citra memperoleh status Tidak Lulus | Berhasil |
| TC04 | Nilai melebihi batas | Nilai 110 | Program menolak nilai dan meminta input ulang | Program menolak nilai 110 dan meminta input ulang | Berhasil |
| TC05 | Data siswa kosong | Tidak ada data siswa | Program menampilkan pesan bahwa belum ada data siswa | Program menampilkan pesan "Belum ada data siswa." | Berhasil |
| TC06 | Menghitung rata-rata | Nilai 80, 70, dan 90 | Rata-rata 80, nilai tertinggi 90, dan nilai terendah 70 | Rata-rata 80.00, nilai tertinggi 90.0, dan nilai terendah 70.0 | Berhasil |
| TC07 | Menyimpan data siswa | Nama Dina, nilai 90 | Data siswa tersimpan dalam file | Data Dina dengan nilai 90 berhasil disimpan ke `data/nilai_siswa.txt` | Berhasil |
| TC08 | Memasukkan input bukan angka | Nilai `abc` | Program menampilkan pesan input tidak valid dan meminta input ulang | Program menampilkan pesan input tidak valid dan meminta input ulang | Berhasil |

## Kesimpulan Pengujian

Berdasarkan pengujian yang telah dilakukan, fitur input data siswa, validasi nilai, penentuan status kelulusan berdasarkan KKM, penampilan daftar siswa, perhitungan analisis nilai, dan penyimpanan data ke dalam file telah berjalan sesuai dengan hasil yang diharapkan.

Dengan demikian, program telah memenuhi fungsi utama yang direncanakan dan seluruh skenario pengujian yang tercantum telah berhasil dijalankan.