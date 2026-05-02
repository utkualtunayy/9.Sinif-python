veri="bilişim teknolojileri"
print(veri)
print(veri[0:7])
print(veri[4:7])
print(veri[8:])
print("----------------------------------------------")
#soru
kelime=input("kelime giriniz")
adet=0
for f in range(0,len(kelime)):
    if kelime[f]=="a":
        adet=adet+1
if adet>0:
    print("a harfi",adet,"kadar vardır")
else:
    print("a harfi yok")