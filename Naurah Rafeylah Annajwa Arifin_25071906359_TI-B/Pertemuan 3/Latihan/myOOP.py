# inheritance

class Produk:
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga

    def info_produk(self):
        print(f"Nama Produk: {self.nama_produk}, dengan harga {self.harga}")

class ProdukElektronik(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        self.garansi = garansi

    def info_produk(self):
        print(f"Nama produk: {self.nama_produk}, dengan harga {self.harga}, dan lama garansi hingga {self.garansi}")

elektronik = ProdukElektronik("Televisi", 35000000, 2027)
elektronik.info_produk()

class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, tanggal_kadarluasa):
        super().__init__(nama_produk, harga)
        self.tanggal_kadarluasa = tanggal_kadarluasa

    def info_produk(self):
        print(f"Nama produk: {self.nama_produk}, dengan harga {self.harga}, dan tanggal kadarluasa {self.tanggal_kadarluasa}")

makanan = ProdukMakanan("Puding", 25000, "30-07-2027")
makanan.info_produk()

# polymorphism

class Notifikasi:
    def __init__(self, song):
        self.song = song

        def kirim(self):
            print("New notification")
        
class Email(Notifikasi):
    def __init__(self, song):
        super().__init__(song)

    def kirim(self):
        print("Send notification via E-mail: New song from Chris Grey")

class SMS(Notifikasi):
    def __init__(self, song):
        super().__init__(song)

    def kirim(self):
        print("Send notification via SMS: New song from Chris Grey")

# encapsulation

class Mahasiswa:
    def __init__(self):
        self.__nilai = 0

    def set_nilai(self, nilai):
        if nilai >= 0 and nilai <= 100:
            self.__nilai = nilai
        else:
            return "Nilai tidak valid"
        
    def get_nilai(self):
        return self.__nilai