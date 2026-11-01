def input_nilai_siswa():
    nama = input("Masukkan nama siswa: ")

    while True:
        try:
            nilai = float(input("Masukkan nilai siswa (0-100): "))

            if 0 <= nilai <= 100:
                return {
                    "nama": nama,
                    "nilai": nilai
                }
            else:
                print("Nilai harus berada di antara 0 sampai 100.")

        except ValueError:
            print("Input tidak valid. Masukkan angka.")