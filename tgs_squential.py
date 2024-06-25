def sequential_search(motor_list, target_motor):
   
    for motor in motor_list:
        if motor['nama'].lower() == target_motor.lower():
            return motor
    return None

# Contoh data motor yang tersedia di toko
motor_list = [
    {"nama": "Honda Supra", "harga": 15000000},
    {"nama": "Yamaha Mio", "harga": 16000000},
    {"nama": "Suzuki Satria", "harga": 17000000},
    {"nama": "Kawasaki Ninja", "harga": 30000000},
    {"nama": "Honda Vario", "harga": 18000000},
    {"nama": "Yamaha NMAX", "harga": 27000000}
]

print("daftar unit motor")
print("1.Honda Supra")
print("2.Yamaha Mio")
print("3.Suzuki Satria")
print("4.Kawasaki Ninja")
print("5.Hoda Vario")
print("6.Yamaha NMAX")
target_motor = input("Masukkan nama unit yang ingin dicari: ")

# Pencarian motor
hasil = sequential_search(motor_list, target_motor)

# Menampilkan hasil pencarian
if hasil is not None:
    print(f"Motor '{target_motor}' ditemukan dengan harga Rp{hasil['harga']:,}.")
else:
    print(f"Motor '{target_motor}' tidak ditemukan dalam daftar motor yang tersedia.")
