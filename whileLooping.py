password = 123
a1 = int(input("masukan password: "))
berapakalisalah = 0
while(a1 != password):
    berapakalisalah += 1
    print("salah")
    a2 = int(input("masukan password lagi/ketik 0 untuk keluar: "))
    if a2 == 0:
        print("keluar")
        break
print("total salah input password : ", berapakalisalah)

