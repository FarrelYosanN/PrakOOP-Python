class Pegawai:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def tampilkan_informasi(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: Rp {self.gaji}")


class Manajer(Pegawai):
    def __init__(self, nama, gaji, tunjangan):
        super().__init__(nama, gaji)
        self.tunjangan = tunjangan

    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print(f"Tunjangan: Rp {self.tunjangan}")


class Programmer(Pegawai):
    def __init__(self, nama, gaji, bonus):
        super().__init__(nama, gaji)
        self.bonus = bonus

    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print(f"Bonus: Rp {self.bonus}")


# Contoh penggunaan:
if __name__ == "__main__":
    pegawai1 = Pegawai("Farrel", 3000000)
    pegawai2 = Pegawai("Arif", 3000000)
    manajer1 = Manajer("Yosan", 8000000, 4000000)
    programmer1 = Programmer("Navyansyah", 6000000, 2500000)
    programmer2 = Programmer("Tono", 6000000, 2500000)
    

    print("\nInformasi Pegawai:")
    pegawai1.tampilkan_informasi()
    
    print("\nInformasi Pegawai:")
    pegawai2.tampilkan_informasi()

    print("\nInformasi Manajer:")
    manajer1.tampilkan_informasi()

    print("\nInformasi Programmer:")
    programmer1.tampilkan_informasi()
    
    print("\nInformasi Programmer:")
    programmer2.tampilkan_informasi()