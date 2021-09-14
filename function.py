def nilai(rata_rata):
    if rata_rata >= 90:
        grade = 'A'
    elif rata_rata >= 75:
        grade = 'B'
    elif rata_rata <= 75:
        grade = 'C'
    else:
        grade = 'D'
    return grade

x =int(input("masukan nilai: "))
grade = nilai(x)
print("grade kamu adalah :", grade)
