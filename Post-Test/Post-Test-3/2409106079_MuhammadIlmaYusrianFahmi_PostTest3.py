BeratBadan = float (input("Masukkan Berat Badan Anda dalam Mg (misal berat anda 53Kg = 53000000) "))
TinggiBadan = float (input("Masukkan Tinggi Badan Anda dalam KM (misal tinggi anda 169cm = 0.00169) "))

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
