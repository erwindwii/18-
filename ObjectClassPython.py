class pabrik:
    def __init__(self, nama, alamat, umur):
        self.nama = nama
        self.alamat = alamat
        self.umur =  umur
    def desc(self):
        print("nama {}, alamat {}, umur {} ".format(self.nama, self.alamat, self.umur))
budi = pabrik("budi", "jl.cikarang", "18")
print(budi.desc())
