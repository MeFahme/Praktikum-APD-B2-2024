"""
This module provides functions for interacting with the operating system.
""" #cuma buat hilangin problem missing docstring

import os

os.system('cls || clear')

akun = {"admin": "admin"}
listsultan = []

while True:
    os.system('cls || clear')
    print("="*40)
    print("MENU UTAMA".center(40))
    print("="*40)
    print("[1] Sign In")
    print("[2] Sign Up")
    print("[3] Exit")
    pilihan = input("\nMasukkan pilihan: ")

    if pilihan == "1":
        BATAS_LOGIN = 3
        IS_LOGIN = False
        while BATAS_LOGIN > 0:
            os.system('cls || clear')
            print("="*40)
            print("LOGIN DULU GAN!".center(40))
            print("="*40)
            username = input("ID\t\t: ")
            password = input("PASSWORD\t: ")
            if username in akun and akun[username] == password:
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
            break

    elif pilihan == "2":
        os.system('cls || clear')
        print("="*40)
        print("BIKIN AKUN DULU GAN!".center(40))
        print("="*40)
        username = input("ID Baru\t\t\t: ")
        if username in akun:
            print("ID sudah ada Gan!")
        else:
            password = input("masukkan password baru\t: ")
            akun[username] = password
            print("AKUN JADI GAN SILAHKAN LOGIN!")
        input("\nKlik enter untuk melanjutkan...")
    elif pilihan == "3":
        os.system('cls || clear')
        print("="*40)
        print("PROGRAM EXIT, TY!".center(40))
        print("="*40)
        IS_LOGIN = False
        exit()
    else:
        print("Pilihan ga ada Gan")
        input("\nKlik enter untuk melanjutkan...")

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
    print("[5] Exit")
    pilihan = input("\nMasukkan pilihan: ")

    if pilihan == "1" and usersekarang == "admin":
        os.system('cls || clear')
        print("="*40)
        print("INPUT NAMA SULTAN".center(40))
        print("="*40)
        sultan = input("Nama Sultan : ")
        roomsultan = input("Room Sultan : ")
        listsultan.append([sultan, roomsultan])
        print()
        print("Nama Sultan berhasil ditambahkan")
        input("\nKlik enter untuk melanjutkan...")

    elif pilihan == "2":
        os.system('cls || clear')
        print("="*40)
        print("CLEAR ROOM".center(40))
        print("="*40)

    elif pilihan == "3":
        os.system('cls || clear')
        print("="*40)
        print("LIST ROOM".center(40))
        print("="*40)

    elif pilihan == "4":
        os.system('cls || clear')
        print("="*40)
        print("GANTI AKUN".center(40))
        print("="*40)
        BATAS_LOGIN = 3
        IS_LOGIN = False
        while BATAS_LOGIN > 0:
            os.system('cls || clear')
            print("="*40)
            print("LOGIN DULU GAN!".center(40))
            print("="*40)
            username = input("ID\t\t: ")
            password = input("PASSWORD\t: ")
            if username in akun and akun[username] == password:
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
        if not IS_LOGIN:
            print("\nGagal login! Kembali ke menu utama.")
            input("\nKlik enter untuk melanjutkan...")


    elif pilihan == "5":
        break

    else:
        print("\nPilihan tidak tersedia! atau anda tidak memiliki akses")
        input("\nKlik enter untuk melanjutkan...")
        break
