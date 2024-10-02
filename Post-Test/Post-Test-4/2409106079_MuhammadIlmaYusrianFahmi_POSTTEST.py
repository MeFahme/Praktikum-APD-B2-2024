userName = "fahmi"
passWord = "79"
gagal = 3


print("PERINGATAN!!! Anda hanya memiliki 3 kali kesempatan untuk login")

while gagal <= 3:
    loginname = input("masukkan username anda : ")
    loginpassword = input("masukkan password sesuai 2 digit terakhir nim anda: ")
    print()

    if loginname == userName and loginpassword == passWord:
        print("login berhasil")
        print()

        print("KALKULATOR BMI")
        BeratBadan = float (input("Masukkan Berat Badan Anda dalam Mg (53Kg = 53000000) = "))
        TinggiBadan = float (input("Masukkan Tinggi Badan Anda dalam KM (169cm = 0.00169) = "))            
        BeratBadanMg = BeratBadan / 1000000
        TinggiBadanMeter = TinggiBadan * 1000
        BodyMassIndex = BeratBadanMg/ (TinggiBadanMeter*TinggiBadanMeter)
      
        if BodyMassIndex < 18.5:
            print (f"Body Mass Index {BodyMassIndex} = Underweight")
        elif BodyMassIndex < 24.9:
            print (f"Body Mass Index {BodyMassIndex} = Normal")
        elif BodyMassIndex < 29.9:
            print (f"Body Mass Index {BodyMassIndex} = Overweight")
        else:
            print (f"Body Mass Index {BodyMassIndex} = Obesitas")
            print()

        lanjut = input("ingin keluar dari program ini ? (Y/N) = ")
        if lanjut == "N":
            continue

        else:
            break

    else:
        gagal-= 1

        if gagal != 0 :
            print(f"batas percobaan sisa {gagal}")
            print()
            
        else:
            print(f"batas percobaan anda telah habis hub admin")
            break
