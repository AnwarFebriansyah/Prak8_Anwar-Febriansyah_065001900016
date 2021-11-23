pertama = int(input("Masukan angka pertama : "))
kedua = int(input("Masukan angka kedua : "))
jumlah=0
for i in range (pertama,(kedua+1),1):
    jumlah+=i
print("Jumlah range adalah "+str(jumlah))