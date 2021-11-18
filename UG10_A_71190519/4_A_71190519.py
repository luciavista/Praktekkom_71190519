artikel = input("Masukkan artikel yang ingin dipindai: ")
namaklub = input("Masukkan nama klub favorit anda: ")
skor = input("Masukkan skor yang ingin dicari: ")

lihat_klub = namaklub in artikel
lihat_skor = skor in artikel

if(lihat_klub and lihat_skor):
    print("Hasil pencarian ditemukan")
elif(lihat_klub and not lihat_skor):
    print("Hanya kata", namaklub, "yang ditemukan pada artikel ini")
elif(not lihat_klub and lihat_skor):
    print("Hanya skor", skor, "yang ditemukan pada artikel ini")
else:
    print("Hasil pencarian", namaklub, "dan", skor, "tidak ditemukan")
