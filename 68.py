şehir="istanbul"
print(şehir[0])#harf alma
len(şehir)
print("----------------------------------------------")

#soru
a=input("isim giriniz:")
if a[0]=="a":
    print("ismin a ile başlar")
else:
    print("a ile başlamıyor")

print("----------------------------------------------")

b=input("bir kelime giriniz")
for cu in range (0,len(b)):
    print("-")

