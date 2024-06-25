def binary_search(mobil_list, target_tahun):
    """
    Fungsi untuk melakukan pencarian biner pada list mobil di toko yang sudah diurutkan berdasarkan tahun.
    
    :param mobil_list: list dari dict yang berisi nama, harga, dan tahun mobil yang sudah diurutkan berdasarkan tahun
    :param target_tahun: tahun mobil yang dicari
    :return: list dari mobil yang ditemukan pada tahun target, atau None jika tidak ditemukan
    """
    low = 0
    high = len(mobil_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_tahun = mobil_list[mid]['tahun']

        if mid_tahun == target_tahun:
            # Mengumpulkan semua mobil yang tersedia pada tahun target
            hasil = []
            # Mencari ke kiri dari mid
            left = mid
            while left >= 0 and mobil_list[left]['tahun'] == target_tahun:
                hasil.append(mobil_list[left])
                left -= 1
            # Mencari ke kanan dari mid
            right = mid + 1
            while right < len(mobil_list) and mobil_list[right]['tahun'] == target_tahun:
                hasil.append(mobil_list[right])
                right += 1
            return hasil
        elif mid_tahun < target_tahun:
            low = mid + 1
        else:
            high = mid - 1

    return None

# Contoh data mobil yang tersedia di toko
mobil_list = [
    {"nama": "Toyota Avanza", "harga": 120000000, "tahun": 1999},
    {"nama": "Honda Civic", "harga": 150000000, "tahun": 1999},
    {"nama": "Suzuki Carry", "harga": 90000000, "tahun": 1999},
    {"nama": "BMW X5", "harga": 850000000, "tahun": 2000},
    {"nama": "Mercedes Benz C200", "harga": 950000000, "tahun": 2000},
    {"nama": "Audi A4", "harga": 720000000, "tahun": 2000},
    {"nama": "Toyota Yaris", "harga": 200000000, "tahun": 2010},
    {"nama": "Honda Jazz", "harga": 250000000, "tahun": 2010},
    {"nama": "Nissan Juke", "harga": 300000000, "tahun": 2010},
    {"nama": "Tesla Model S", "harga": 1500000000, "tahun": 2018},
    {"nama": "Ford Mustang", "harga": 1800000000, "tahun": 2018},
    {"nama": "Chevrolet Camaro", "harga": 1600000000, "tahun": 2018},
    {"nama": "Toyota Fortuner", "harga": 500000000, "tahun": 2020},
    {"nama": "Mitsubishi Pajero", "harga": 600000000, "tahun": 2020},
    {"nama": "Honda CRV", "harga": 450000000, "tahun": 2020}
]

# Mengurutkan data mobil berdasarkan tahun
mobil_list = sorted(mobil_list, key=lambda x: x['tahun'])

print("cari tahun mobil")
print("1999")
print("2000")
print("2010")
print("2018")
print("2020")
target_tahun = int(input("Masukkan tahun mobil yang ingin dicari: "))

# Pencarian mobil
hasil = binary_search(mobil_list, target_tahun)

# Menampilkan hasil pencarian
if hasil is not None:
    print(f"Mobil-mobil yang tersedia pada tahun {target_tahun}:")
    for mobil in hasil:
        print(f"- {mobil['nama']} dengan harga Rp{mobil['harga']:,}")
else:
    print(f"Tidak ada mobil yang tersedia pada tahun {target_tahun}.")
