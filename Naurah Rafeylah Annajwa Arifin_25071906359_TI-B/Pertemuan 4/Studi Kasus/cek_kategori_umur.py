try:
    umur = int(input("Masukkan umur Anda: "))

    if umur < 0:
        raise ValueError("Umur tidak boleh berupa bilangan negatif")
    
    if umur <= 12:
        kategori = "Anak-anak"
    elif umur <= 17:
        kategori = "Remaja"
    elif umur <= 59:
        kategori = "Dewasa"
    else:
        kategori = "Lansia"
    
except ValueError as e:
    print("Terjadi kesalahan. Error:", e)

else: 
    print("Kategori umur Anda adalah:", kategori)

finally:
    print("Program selesai")