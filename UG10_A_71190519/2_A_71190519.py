print("############################")
print("Kalkulator Advance Sederhana")
print("############################")
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")

menu = int(input("Masukkan menu yang anda pilih: "))

#Menghitung sisa hasil bagi antara dua bilangan
if menu == 1:
    bil1 = float(input("Masukkan bilangan yang ingin dibagi: "))
    bil2 = float(input("Masukkan bilangan pembagi: "))
    
    sisabagi = bil1 % bil2
    
    print("Sisa hasil bagi", bil1, "dibagi dengan", bil2, "adalah", sisabagi)

#Menghitung hasil bagi antara dua bilangan
elif menu == 2:
    bil1 = float(input("Masukkan bilangan yang ingin dibagi: "))
    bil2 = float(input("Masukkan bilangan pembagi: "))

    hasilbagi = bil1 // bil2

    print("Hasil pembagian", bil1, "dibagi dengan", bil2, "dibulatkan kebawah adalah", hasilbagi)

#Menghitung akar kubik sebuah bilangan
elif menu == 3:
    bil1 = float(input("Masukkan bilangan yang ingin dicari akar kubiknya: "))

    akarkubik = bil1 **(1/3)

    print("Akar kubik dari", bil1, "adalah", akarkubik)
else:
    print("Menu yang anda pilih tidak tersedia")
    
