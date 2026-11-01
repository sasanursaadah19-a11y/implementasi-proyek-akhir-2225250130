KKM = 75


def hitung_rata_rata(data_siswa):
    if len(data_siswa) == 0:
        return 0

    total_nilai = sum(siswa["nilai"] for siswa in data_siswa)
    return total_nilai / len(data_siswa)


def cari_nilai_tertinggi(data_siswa):
    if len(data_siswa) == 0:
        return 0

    return max(siswa["nilai"] for siswa in data_siswa)


def cari_nilai_terendah(data_siswa):
    if len(data_siswa) == 0:
        return 0

    return min(siswa["nilai"] for siswa in data_siswa)


def tentukan_status(nilai):
    if nilai >= KKM:
        return "Lulus"
    else:
        return "Tidak Lulus"