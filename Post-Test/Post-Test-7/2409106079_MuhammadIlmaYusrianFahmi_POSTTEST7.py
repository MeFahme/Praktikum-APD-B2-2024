
"""
This module provides functions for interacting with the operating system.
""" #buat hilangin problem missing docstring
import os
from colorama import Fore
print(Fore.CYAN)
akun = {"admin":"admin"}
listsultan = {}
IS_LOGIN = False
BATAS_LOGIN = 3
rooms = [f"{r}" for r in range(1,11)]

def clear():
    """clear terminal"""
    os.system('cls || clear')

def main_menu():
    """show menu"""
    clear()
    print("="*30)
    print("MAIN MENU".center(30))
    print("="*30)
    print("[1] SIGN IN")
    print("[2] SIGN UP")
    print("[3] EXIT")

def admin_menu():
    """admin menu"""
    clear()
    print("="*30)
    print("SULTAN GAMING CENTRE".center(30))
    print("="*30)
    print("[0] Ganti Password Akun")
    print("[1] Booking Room")
    print("[2] Clear Room")
    print("[3] Clear All Room")
    print("[4] List Room Sultan")
    print("[5] Room Kosong")
    print("[6] Log Out")
    print("[7] Exit")

def user_menu():
    """user menu"""
    clear()
    print("="*30)
    print("SULTAN GAMING CENTRE".center(30))
    print("="*30)
    print("[4] List Room Sultan")
    print("[5] Room Kosong")
    print("[6] Log Out")
    print("[7] Exit")

def login(user_akun):
    """login"""
    clear()
    BATAS_LOGIN = 3
    while BATAS_LOGIN > 0:
        clear()
        print("="*30)
        print("MAIN MENU".center(30))
        print("="*30)
        username = input("ID\t\t: ")
        password = input("PASSWORD\t: ")
        if username in user_akun and user_akun[username] == password:
            print(f"\nBerhasil Login! anda login sebagai {username}")
            input("\nKlik enter untuk menlanjutkan...")
            return True, username
        BATAS_LOGIN -= 1
        print("\nID atau PASSWORD salah!")
        print(f"\nKesempatan login tersisa {BATAS_LOGIN} kali lagi!")
        input("\nKlik enter untuk menlanjutkan...")
        clear()
    print("\nANDA GAGAL LOGIN 3 KALI. HUBUNGI ADMIN")
    exit()

def bikin_akun(user_akun):
    """bikin akun"""
    clear()
    print("="*30)
    print("BIKIN AKUN DULU GAN!".center(30))
    print("="*30)
    username = input("ID BARU\t\t: ")
    if username in user_akun:
        print("ID sudah ada GAN!")
    else:
        password = input("PASSWORD Baru\t: ")
        akun[username] = password
        print("AKUN JADI SILAHKAN LOGIN GAN!")
    input("\nKlik enter untuk menlanjutkan...")

def room_kosong(rooms):
    """daftar room tersedia"""
    clear()
    print("="*30)
    print("LIST ROOM KOSONG".center(30))
    print("="*30)
    for r, room in enumerate(rooms[:10]):
        print(f"{r+1}. {room}")
    input("\nKlil Enter untuk melanjutkan...")

def booking_room(listsultan_room):
    """booking room"""
    clear()
    print("="*30)
    print("LIST SULTAN MAU BOOKING ROOM".center(30))
    print("="*30)
    sultan = input("Nama Sultan\t: ")
    if sultan != "0":
        roomsultan = input("Nomor Room\t: ")
        if roomsultan in listsultan_room.values():
            print("\nRoom sedang digunakan")
        else:
            if roomsultan in rooms:
                listsultan_room[sultan] = roomsultan
                rooms.remove(roomsultan)
                print("Nama Sultan Berhasil ditambahkan")
            else:
                print("Room tidak ada")
        input("\nKlik enter untuk melanjutkan...")

def list_akun():
    """list akun"""
    clear()
    print("LIST AKUN".center(30))
    print("="*30)
    print("NO. | \t ID\t |\t Pass")
    print("-"*30)
    for u, (username, password) in enumerate(akun.items()):
        print(f"{u+1}\t {username}\t\t {password}")
    ganti_password = input("\nPilih nomor akun yang ingin diubah: ")
    if ganti_password.isdigit() and 0 < int(ganti_password) <= len(akun):
        pilih = list(akun.keys()) [int(ganti_password) -1]
        password_baru = input("Masukkan password baru: ")
        if password_baru:
            akun.update({pilih: password_baru})
            print("Password berhasil diubah")
            # input("\nKlik enter untuk melanjutkan...")
        else:
            print("Password tidak boleh kosong")
    else:
        print("\nPilihan tidak valid")
    input("\nKlik enter untuk melanjutkan...")

def clear_room():
    """clear room"""
    clear()
    print("="*30)
    print("CLEAR ROOM SULTAN".center(30))
    print("="*30)
    print("NO. | \t Sultan\t |\tRoom")
    print("-"*30)
    for index, (sultan, room) in enumerate(listsultan.items()):
        print(f"{index+1}\t {sultan}\t\t {room}")
    input_string = input("\nPilih nomor Room. [0 = kembali] : ")

    if not input_string.isdigit():
        print("input tidak valid")
        input("\nKlik enter untuk menlanjutkan...")
        return

    index = int(input_string) - 1

    if index == -1:
        return
    elif 0 <= index < len(listsultan):
        hapusroom = list(listsultan.keys())[index]
        room_clear = listsultan.pop(hapusroom)
        rooms.append(room_clear)
        clear()
        print("Room berhasil dikosongkan")
    else:
        print("input tidak valid")
    input("\nKlik enter untuk menlanjutkan...")

def list_room():
    """list room"""
    clear()
    print("="*30)
    print("LIST ROOM PARA SULTAN".center(30))
    print("="*30)
    print("NO. | \t Sultan\t |\tRoom")
    print("-"*30)
    for index, (sultan, room) in enumerate(listsultan.items()):
        print(f"{index+1}\t {sultan}\t\t {room}")
    input("\nKlik enter untuk menlanjutkan...")

def clearall_room(listsultan, rooms):
    """rekursif"""
    if not listsultan:
        return
    else:
        room = listsultan.popitem()[1]
        rooms.append(room)
        clearall_room(listsultan, rooms)
        clear()


while True:
    clear()
    main_menu()
    pilihan = input("\nMasukkan Pilihan: ")
    if pilihan == "1":
        IS_LOGIN, usersekarang = login(akun)
        if IS_LOGIN:
            while IS_LOGIN:
                clear()
                if usersekarang == "admin":
                    admin_menu()
                else:
                    user_menu()
                pilihan = input("\nMasukkan pilihan: ")

                if pilihan == "0" and usersekarang == "admin":
                    list_akun()

                elif pilihan == "1" and usersekarang == "admin":
                    booking_room(listsultan)

                elif pilihan == "2" and usersekarang == "admin":
                    clear_room()

                elif pilihan == "3" and usersekarang == "admin":
                    clearall_room(listsultan, rooms)
                    print("DONE!!!")
                    input("\nKlik enter untuk melanjutkan...")

                elif pilihan == "4":
                    list_room()

                elif pilihan == "5":
                    room_kosong(rooms)


                elif pilihan == "6":
                    IS_LOGIN = False

                elif pilihan == "7":
                    clear()
                    exit()

                else:
                    print("\nPilihan tidak tersedia / Admin Only")
                    input("\nKlik enter untuk melanjutkan...")

    elif pilihan == "2":
        bikin_akun(akun)

    elif pilihan == "3":
        IS_LOGIN = False
        clear()
        break

    else:
        print("PILIHAN GADA GAN")
        input("\nKlik enter untuk menlanjutkan...")
        continue
