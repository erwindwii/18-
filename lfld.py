#fungsi,looping,function,dict
data_nama = [] #variabel global

def show_data(): #cek panjang 
    if len(data_nama) < 0:
        print("data kosong !")
    else:
        print("data terisi")
        print(data_nama)
    
def insert_data():
    new_data = str(input("masukan nama baru :"))
    data_nama.append(new_data)
    print("data sudah terisi", data_nama)
    looping()

def awalan():   
    print("Welcome to mall, silahkan masukan nama dibawah")
    nama = str(input("Nama :"))
    data_nama.append(nama)

def looping():
    print("exit atau kembali? :")
    yesNo = int(input("1 or 0 :"))
    if yesNo == 1:
        awalan()
    if yesNo == 0:
        exit()
        
awalan()
pilihan = int(input("1.cek data\n2.insert data\n silahkan pilih :"))
if pilihan == 1:
    show_data()
    looping()
elif pilihan == 2:
    insert_data()
else:
    print("inputan salah!")
    
    

