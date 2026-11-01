from src.input_data import input_nilai_siswa
from src.proses import (
    hitung_rata_rata,
    cari_nilai_tertinggi,
    cari_nilai_terendah,
    tentukan_status
)
from src.output import (
    tampilkan_daftar_siswa,
    tampilkan_analisis,
    simpan_data_siswa
)


data_siswa = []


def tambah_data_siswa():
    siswa = input_nilai_siswa()
    siswa["status"] = tentukan_status(siswa["nilai"])
    data_siswa.append(siswa)

    simpan_data_siswa(data_siswa)

    print("Data siswa berhasil ditambahkan.")


def tampilkan_semua_data():
    tampilkan_daftar_siswa(data_siswa)


def tampilkan_hasil_analisis():
    if len(data_siswa) == 0:
        print("\nBelum ada data untuk dianalisis.")
        return

    rata_rata = hitung_rata_rata(data_siswa)
    tertinggi = cari_nilai_tertinggi(data_siswa)
    terendah = cari_nilai_terendah(data_siswa)

    tampilkan_analisis(rata_rata, tertinggi, terendah)


def menu_utama():
    while True:
        print("\n=== PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA SISWA ===")
        print("1. Tambah data siswa")
        print("2. Tampilkan daftar siswa")
        print("3. Tampilkan analisis nilai")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_data_siswa()
        elif pilihan == "2":
            tampilkan_semua_data()
        elif pilihan == "3":
            tampilkan_hasil_analisis()
        elif pilihan == "4":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-4.")


if __name__ == "__main__":
    menu_utama()