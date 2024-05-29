class Katak:
    def __init__(self, jenis, cara_bergerak):
        self.jenis = jenis
        self.cara_bergerak = cara_bergerak

    def tampilkan_informasi(self):
        print(f"-Jenis: {self.jenis}")
        print(f"-Cara Bergerak: {self.cara_bergerak}")


class Kecebong(Katak):
    def __init__(self, jenis, cara_bergerak, panjang_ekor):
        super().__init__(jenis, cara_bergerak)
        self.panjang_ekor = panjang_ekor

    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print(f"-Panjang Ekor: {self.panjang_ekor} mm")


# Contoh penggunaan:
if __name__ == "__main__":
    katak1 = Katak("Katak Lembu", "Melompat")
    kecebong1 = Kecebong("Kecebong Air", "Bergerak dengan sirip", 3.2)

    print("Informasi Katak:")
    katak1.tampilkan_informasi()

    print("\nInformasi Kecebong:")
    kecebong1.tampilkan_informasi()