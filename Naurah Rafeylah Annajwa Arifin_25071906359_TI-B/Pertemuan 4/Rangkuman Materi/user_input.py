# input dgn baris baru
print("Masukkan nama:")
name = input()
print(f"Hello {name}")

# menggunakan prompt dibaris yg sama
name = input("Masukkan nama:")
print(f"Hello {name}")

# mutiple input
name = input("Masukkan nama:")
print(f"Hello {name}")
fav1 = input("Hewan yang kamu sukai::")
fav2 = input("Warna yang kamu sukai:")
fav3 = input("Angka keberuntunganmu:")
print(f"Kamu mau {fav1} {fav2} dengan {fav3} kaki?")

# input numbers
kaki1 = float(input("Masukkan panjang kaki pertama: "))
kaki2 = float(input("Masukkan panjang kaki kedua: "))
hypo = (kaki1**2 + kaki2**2) **.5
print("Panjang hipotenusa adalah", hypo)

# string to int
string_input = input("Masukkan angka: ")
integer_number = int(string_input)
print("Bilangan bulat: ", integer_number)

# string to float
string_input = input("Masukkan bilangan desimal: ")
float_number = float(string_input)
print("Bilangan desimal: ", float_number)

# string to boolean
string_input = input("Masukkan Benar atau Salah: ")
boolean_value = string_input == 'True'
print("Boolean", boolean_value)