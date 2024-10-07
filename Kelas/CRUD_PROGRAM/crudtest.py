"""
This module provides functions for interacting with the operating system.
""" #cuma buat hilangin problem missing docstring

import os

os.system('cls || clear')

User = {"admin": "admin"}

listsultan = []

while True:
    BATAS_LOGIN = 3
    IS_LOGIN =   False

    while BATAS_LOGIN > 0:
        os.system('cls || clear')
        print("="*40)
        print("LOGIN DULU GAN!".center(40))
        print("="*40)
        username = input("ID\t\t: ")
        password = input("PASSWORD\t: ")
        if username in User and User[username] == password:
            IS_LOGIN = True
            usersekarang = username
            os.system("cls || clear")
            print(f"\nBerhasil login! anda login sebagai {username}")
            input("\nKlik enter untuk melanjutkan...")
            break
        BATAS_LOGIN -= 1
        print("\nUsername atau password salah!")
        print(f"\nKesempatan login tersisa {BATAS_LOGIN} kali lagi!")
        input("\nKlik enter untuk melanjutkan...")

    if IS_LOGIN:
        while IS_LOGIN:
            os.system('cls || clear')
            print("="*40)
            print("SULTAN GAMING CENTRE".center(40))
            print("="*40)

            if usersekarang == "admin":
                print("[1] Booking Room")
                print("[2] Clear Room")
            print("[3] Lihat Room yang Tersedia")
            print("[4] Ganti Akun")
            print("[5] Exit Program")
            pilihan = input("\nMasukkan pilihan: ")

            if pilihan == "1" and usersekarang == "admin":
                os.system('cls || clear')
                print("="*40)
                print("INPUT NAMA SULTAN".center(40))
                print("="*40)
                # program menambahkan daftar nama para sultan
                sultan = input("Nama Sultan : ")
                roomsultan = input("Room Sultan : ")
                listsultan.append([sultan, roomsultan])
                print()
                print("nama sultan telah ditambahkan")
                input("\nKlik enter untuk melanjutkan...")


            elif pilihan == "2" and usersekarang == "admin":
                os.system('cls || clear')
                print("="*40)
                print("KOSONGKAN ROOM".center(40))
                print("="*40)
                # program menghapus room
                for index, sultan in enumerate(listsultan):
                    print("NO. | \t Sultan\t |\tRoom")
                    print(f"{index+1}\t {sultan[0]}\t\t {sultan[1]}")

                #untuk menyimpan input sebagai string
                input_string = input("\nPilih nomor sultan yang pulang. [0 = kembali] : ")

                #untuk memastikan input adalah digit
                if not input_string.isdigit():
                    print("input tidak valid")
                    input("\nKlik enter untuk melanjutkan...")
                    continue

                #konversi jadi integer setelah input adalah digit
                index = int(input_string) -1

#jadi program ga error kalau inputnya kosong misalnya langsung dienter atau input ga valid
                if index == -1:
                    continue
                elif 0 <= index < len(listsultan):
                    listsultan.pop(index)
                else:
                    print("input tidak valid")
                input("\nKlik enter untuk melanjutkan...")

            elif pilihan == "3":
                os.system('cls || clear')
                print("="*40)
                print("Room Para Sultan".center(40))
                print("="*40)
                # program melihat daftar nama para sultan
                for index, sultan in enumerate(listsultan):
                    print("NO. | \t Sultan\t|\tRoom")
                    print(f"{index+1}\t {sultan[0]}\t\t {sultan[1]}")
                input("\nKlik enter untuk melanjutkan...")

            elif pilihan == "4":
                os.system("cls || clear")
                print("Anda telah Logout!")
                print()
                input("\nKlik enter untuk melanjutkan...")
                break
            elif pilihan == "5":
                os.system("cls || clear")
                print("TERIMAKASIH!".center(40))
                print()
                IS_LOGIN = False
                exit()
            else:
                print("\nPilihan tidak tersedia! atau ADMIN ONLY")
                input("\nKlik enter untuk melanjutkan...")
    else:
        os.system("cls || clear")
        print("="*40)
        print("ANDA GAGAL LOGIN, HUBUNGI ADMIN".center(40))
        print("="*40)
        break
