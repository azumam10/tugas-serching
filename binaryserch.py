def binary_serch(arr, x):
    
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low)// 2

    #    jika elemen berada di tengah
        if arr[mid]<x:
            low = mid + 1

    # jika elemen berada di sebelah kiri tengah
        elif arr[mid]>x:
            high = mid - 1

    # elemen di temukan
        else:
            return mid
    # jika elemen tidak di temukan
    return -1


def main():
    # menerima input daftar elemen yang sudah terurut dari pengguna
    arr = list(map(int,input("masukan daftar elemen yang sudah terurut (pisahkan dengan spasi): ").split()))

    # menerima input elemen yang akan dicari
    x = int(input("masukan elemen yang di cari:"))

    reslut = binary_serch(arr, x)

    if reslut != -1:
        print(f'elemen yang ditemukan pada indeks {reslut}')
    else:
        print("elemen tidak ditemukan dalam dafrae")


# menjalankan fungsi utama
if __name__=="__main__":
    main()