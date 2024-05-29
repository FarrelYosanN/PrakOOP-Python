class PersegiPanjang:
    def __init__(self, panjang=0, lebar=0):
        self.panjang = panjang
        self.lebar = lebar

    def getLuas(self):
        return self.panjang * self.lebar

    def getKeliling(self):
        return 2 * (self.panjang + self.lebar)

class HitungPersegiPanjang:
    def __init__(self):
        self.panjang = 8.0
        self.lebar = 9.0
        self.persegi_panjang = PersegiPanjang(self.panjang, self.lebar)

    def run(self):
        print("-----Belajar Konstruktor-----")
        print("Program Persegi Panjang")
        print("----------------------------------")
        print("Panjang persegi panjang : {}".format(self.panjang))
        print("Lebar persegi panjang : {}".format(self.lebar))
        print("Luas persegi panjang : {}".format(self.persegi_panjang.getLuas()))
        print("Keliling persegi panjang: {}".format(self.persegi_panjang.getKeliling()))

if __name__ == "__main__":
    hitung_persegi_panjang = HitungPersegiPanjang()
    hitung_persegi_panjang.run()