def tampilkan_daftar_siswa(data_siswa):
    if len(data_siswa) == 0:
        print("\nBelum ada data siswa.")
        return

    print("\n=== DAFTAR NILAI SISWA ===")
    print("-" * 45)

    for nomor, siswa in enumerate(data_siswa, start=1):
        print(f"{nomor}. Nama  : {siswa['nama']}")
        print(f"   Nilai : {siswa['nilai']}")
        print(f"   Status: {siswa['status']}")
        print("-" * 45)


def tampilkan_analisis(rata_rata, tertinggi, terendah):
    print("\n=== HASIL ANALISIS NILAI ===")
    print(f"Rata-rata       : {rata_rata:.2f}")
    print(f"Nilai tertinggi : {tertinggi}")
    print(f"Nilai terendah  : {terendah}")


def simpan_data_siswa(data_siswa):
    with open("data/nilai_siswa.txt", "w", encoding="utf-8") as file:
        for siswa in data_siswa:
            file.write(
                f"{siswa['nama']},{siswa['nilai']},{siswa['status']}\n"
            )

    print("Data siswa berhasil disimpan ke file.")