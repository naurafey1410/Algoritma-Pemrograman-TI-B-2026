# try except
try:
  print(x)
except:
  print("Terjadi kesalahan")

# dengan 2 except
try:
  print(x)
except NameError:
  print("Variabel tidak ditemukan")
except:
  print("Terdapat kesalahan lain")

# else
try:
  print("Hello")
except:
  print("Terdapat kesalahan")
else:
  print("Tidak terdapat kesalahan")

# finally
try:
  print(x)
except:
  print("Terjadi kesalahan")
finally:
  print("Proses try-except selesai")

# raise
umur = -1

if umur < 0:
  raise Exception("Umur tidak boleh negatif")

