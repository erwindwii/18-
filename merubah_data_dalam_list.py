#tutorial meerubah isi list dengan metode insert 
#insert(index, item) menambahkan item dari indeks tertentu

cs = ["Anggun", "Dian", "Agung", "Adi", "Adam"]
print("list yang tersedia", cs,"merubah isi list (index,item)")
index = int(input("index:"))
item = str(input("kata baru:"))
cs.insert(index,item)
print("new list", cs)


