# Fungsi rekursif ini sesuai namanya fungsi yang berulang ulang
#dengan cara dia manggil
# dirinya sendiri selama proses eksekusi untuk menyelesaikan suatu masalah.
# Fungsi rekursif biasanya digunakan
# untuk memecah masalah besar menjadi masalah yang lebih kecil,
# yang secara berulang diselesaikan hingga mencapai kondisi dasar (base case)
# di mana proses rekursi berhenti.

# Konsep utama dalam rekursi meliputi dua hal penting:
# Base case: Kondisi penghentian rekursi, yang menghentikan pemanggilan fungsi lebih lanjut. Ini adalah langkah yang mencegah rekursi berjalan tanpa henti.
# Recursive case: Bagian dari fungsi yang terus memanggil dirinya sendiri dengan input yang sedikit berubah, biasanya mendekati kondisi dasar.


#ini contohnya fungsi faktorial
def faktorial(angka):
    #base case
    if angka == 0 or angka == 1: # 2. disini dicek nihh kalau angka nya 0/1 dia
        return 1 #2. kembaliin nilai 1 #karena nilai kita masih 5 berarti

    #rekursif case

    else: #2. masuk ke else
        return angka * faktorial(angka - 1)
     #3. disini kita ngembaliin nilai angka = 5 dengan dikali fungsi faktorial(angka-1)
     # jadinya gini 5 * faktorial(5-1) * faktorial(4-1) * dst(3-1) * (2-1)* (nilai kita udah 1 jadi return 1)
     # 5*4*3*2*1 = 120

print(faktorial(5))  #4. akan output 120
#1. disini kita panggil fungsinya angka = 5





#fungsi rekursif ini bisa dipake juga untuk ngeprint list
list_data = [10, 20, 30, 40, 50]

def cetak_list(list, index=0):
    # Base case: jika index sudah mencapai panjang list, berhenti
    if index == len(list):
        return
    # Cetak elemen list pada index sekarang
    print(list[index])
    # Panggil fungsi secara rekursif untuk index berikutnya
    cetak_list(list, index + 1)

# Contoh penggunaan
cetak_list(list_data)
#bisa diimplementasikan sesuai kreatifitas kalian