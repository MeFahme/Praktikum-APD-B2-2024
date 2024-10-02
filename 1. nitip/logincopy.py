userName = "fahmi"
passWord = "79"
gagal = 0
maxGagal = 2

print("PERINGATAN!!! Anda hanya memiliki 3 kali kesempatan untuk login")
while True:
    while gagal <= 2:
        loginname = input("masukkan username anda : ")
        loginpassword = input("masukkan password sesuai 2 digit terakhir nim anda: ")
        print()
        gagal += 1
        if loginname == userName and loginpassword == passWord:
            print("login berhasil")
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

            opsi = input("ingin berhenti ? 1. ya 2. tidak \npilih nomor 1/2 : ")
            if opsi == "1":
                break
    else:
        print("Anda telah mencapai batas maksimum login, mohon hubungi admin")
    break