UG = float(input("Masukkan nilai rata-rata UG anda: "))
TTS = float(input("Masukkan nilai TTS anda: "))
TAS = float(input("Masukkan nilai TAS anda: "))
print("=========================")
#UG 70% : 0.7
#TTS 15% : 0.15
#TAS 15% : 0.15
nilai = ((UG*0.7)+(TTS*0.15)+(TAS*0.15))

print("Nilai anda: ", str(nilai))

if nilai >= 85:
    print("Nilai huruf anda: A")
elif nilai >= 80:
    print("Nilai huruf anda: A-")
elif nilai >= 75:
    print("Nilai huruf anda: B+")
elif nilai >= 70:
    print("Nilai huruf anda: B")
elif nilai >= 65:
    print("Nilai huruf anda: B-")
elif nilai >= 60:
    print("Nilai huruf anda: C+")
elif nilai >= 55:
    print("Nilai huruf anda: C")
elif nilai >= 45:
    print("Nilai huruf anda: D")
else:
    print("Nilai huruf anda: E")

    
