#menghapus item dari list dengan remove()
#gunakan nama item bukan nilai index
cs = ["Anggun", "Dian", "Agung", "Adi", "Adam"]
print("list yang tersedia", cs,"menghapus item dari list (index)")
index = str(input("index:"))
cs.remove(index)
print("new list", cs)
