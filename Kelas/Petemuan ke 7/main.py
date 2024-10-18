import os

os.system('cls || clear')

mahasiswa = ["Steven", "Michael", "Selyn"]
kesempatan = 3
isLogin = False

def hapus():
    for i, data in enumerate(mahasiswa, 1):
        print(f"[{i}] {data}")
    index = int(input("\nMasukkan index nama yang ingin diubah: ")) - 1
    deleted_mahasiswa = mahasiswa.pop(index)
    print(f"\n[{deleted_mahasiswa}] berhasil dihapus!")

while kesempatan > 0:
    os.system('cls || clear')
    print("="*40)
    print("Login Form".center(40))
    print("="*40)
    username = input("Masukkan nama akun\t: ")
    password = input("Masukkan password\t: ")
    if username.lower() == "admin" and password == "admin":
        isLogin = True
        print("\nBerhasil login!")
        input("\nKlik enter untuk melanjutkan...")
        break
    kesempatan -= 1
    print("\nUsername atau password salah!")
    print(f"\nKesempatan login tersisa {kesempatan} kali lagi!")
    input("\nKlik enter untuk melanjutkan...")

if isLogin:
    while isLogin:
        os.system('cls || clear')
        print("="*40)
        print("Program CRUD Daftar Mahasiswa".center(40))
        print("="*40)
        print("[1] Lihat Daftar Nama Mahasiswa")
        print("[2] Tambah Nama Mahasiswa")
        print("[3] Edit Nama Mahasiswa")
        print("[4] Hapus Nama Mahasiswa")
        print("[5] Keluar Program")
        pilihan = input("\nMasukkan pilihan: ")

        if pilihan == "1":
            os.system('cls || clear')
            print("="*40)
            print("Daftar Nama Mahasiswa".center(40))
            print("="*40)
            # nomor = 1
            for i, data in enumerate(mahasiswa, 1):
                print(f"[{i}] {data}")
                # nomor += 1

            for i in range(len(mahasiswa)):
                print(f"{i+1}. {mahasiswa[i]}")    
            
            input("\nKlik enter untuk melanjutkan...")
        elif pilihan == "2":
            os.system('cls || clear')
            print("="*40)
            print("Tambah Nama Mahasiswa".center(40))
            print("="*40)
            mahasiswa_baru = input("\nMasukkan nama mahasiswa: ")
            mahasiswa.append(mahasiswa_baru)
            print(f"\nNama [{mahasiswa_baru}] mahasiswa baru berhasil ditambahkan!")
            input("\nKlik enter untuk melanjutkan...")


        elif pilihan == "3":
            os.system('cls || clear')
            print("="*40)
            print("Edit Nama Mahasiswa".center(40))
            print("="*40)

            for i, data in enumerate(mahasiswa, 1):
                print(f"[{i}] {data}")
            index = int(input("\nMasukkan index nama yang ingin diubah\t: ")) - 1
            nama_baru = input("Masukkan nama mahasiswa baru\t\t: ")
            mahasiswa[index] = nama_baru
            print("\nNama mahasiswa berhasil diubah!")
            input("\nKlik enter untuk melanjutkan...")


        elif pilihan == "4":
            os.system('cls || clear')
            print("="*40)
            print("Hapus Nama Mahasiswa".center(40))
            print("="*40)
            # for i, data in enumerate(mahasiswa, 1):
            #     print(f"[{i}] {data}")
            # index = int(input("\nMasukkan index nama yang ingin diubah: ")) - 1
            # deleted_mahasiswa = mahasiswa.pop(index)
            # print(f"\n[{deleted_mahasiswa}] berhasil dihapus!")
            hapus()
            input("\nKlik enter untuk melanjutkan...")

        elif pilihan == "5":
            break
        else:
            print("\nPilihan tidak tersedia!")
            input("\nKlik enter untuk melanjutkan...")
else:
    os.system("cls || clear")
    print("Kesempatan login sudah habis! Keluar dari program!")

os.system("cls || clear")
print("="*40)
print("Program Selesai!".center(40))
print("="*40)