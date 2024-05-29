class Tabungan:
    def __init__(self, saldo):
        self.saldo = saldo

    def simpanTabungan(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
        else:
            print("Jumlah simpan harus lebih dari 0")

    def ambilTabungan(self, jumlah):
        if jumlah > 0 and jumlah <= self.saldo:
            self.saldo -= jumlah
        elif jumlah <= 0:
            print("Jumlah ambil harus lebih dari 0")
        else:
            print("Saldo tidak mencukupi")

    def sisaSaldo(self):
        return self.saldo

class HitungTabungan:
    def __init__(self):
        self.saldo_awal = 2000000
        self.tabungan = Tabungan(self.saldo_awal)

    def run(self):
        print("-" * 50)
        print("SELAMAT DATANG DI BANK ABC")
        print("-" * 50)
        print("Sisa saldo Anda saat ini adalah : Rp.", self.saldo_awal)
        print("-" * 50)
        self.tabungan.simpanTabungan(500000)
        print("Sisa saldo Anda saat ini adalah : Rp.", self.tabungan.sisaSaldo())
        print("-" * 50)
        self.tabungan.ambilTabungan(600000)
        print("Sisa saldo Anda : Rp.", self.tabungan.sisaSaldo())
        print("-" * 50)

if __name__ == "__main__":
    hitung_tabungan = HitungTabungan()
    hitung_tabungan.run()