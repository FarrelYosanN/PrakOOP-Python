class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampilkan_informasi(self):
        print(f"-Nama: {self.nama}")
        print(f"-Umur: {self.umur} tahun")


class Dosen(Orang):
    def __init__(self, nama, NIP, umur):
        super().__init__(nama, umur)
        self.NIP = NIP

    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print(f"-NIP: {self.NIP}")


# Contoh penggunaan:
if __name__ == "__main__":
    orang1 = Orang("Farrel", 21)
    orang2 = Orang("Yosan", 20)
    dosen1 = Dosen("Bapak Budi", 1990992993, 42)
    dosen2 = Dosen("Bapak Imron", 1990992994, 44)
    dosen3 = Dosen("Bapak Roni", 1990992995, 40)

    print("\nInformasi Orang:")
    orang1.tampilkan_informasi()
    
    print("\nInformasi Orang:")
    orang2.tampilkan_informasi()

    print("\nInformasi Dosen:")
    dosen1.tampilkan_informasi()
    
    print("\nInformasi Dosen:")
    dosen2.tampilkan_informasi()
    
    print("\nInformasi Dosen:")
    dosen3.tampilkan_informasi()