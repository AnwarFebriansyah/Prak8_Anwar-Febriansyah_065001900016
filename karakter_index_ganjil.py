print("PROGRAM MEMUNCULKAN KARAKTER INDEX GANJIL")
kata = input("Masukan sebuah kata: ")
karakterindexganjil=""
for i in range(len(kata)):
    if i%2!=0:
        karakterindexganjil+=kata[i]
print(karakterindexganjil)