input1 = input("Mendatar/Menurun?: ")

if input1 == "Mendatar":
    input2 = int(input("Masukkan kolom: "))
    print("#"* input2)
elif input1 == "Menurun":
    input2 = int(input("Masukkan baris: "))
    print("*\n"* input2)
else:
    print("Pola tidak dikenali")
