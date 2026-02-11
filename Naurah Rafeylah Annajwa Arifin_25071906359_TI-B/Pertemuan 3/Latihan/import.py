import myOOP

p1 = myOOP.ProdukElektronik("Televisi", 35000000, 2027)
p2 = myOOP.ProdukMakanan("Puding", 25000, "30-07-2027")
p1.info_produk()
p2.info_produk()

x = myOOP.Email("Send notification via E-mail: New song from Chris Grey")
x.kirim()

mhs1 = myOOP.Mahasiswa()
mhs2 = myOOP.Mahasiswa()
mhs1.set_nilai(87)
print(mhs1.get_nilai())
print(mhs2.set_nilai(110))
mhs2.get_nilai()