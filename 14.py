#in oparatörü
hafta_ici=["pazartesi","salı","çarşamba","perşembe","cuma"]
print( "cuma" in hafta_ici)
print( "cumartesi" in hafta_ici)
print("haftaiçi günlerinin eleman sayısı:",len(hafta_ici))
hafta_ici.append(5)#sona eleman eklemek için
print(hafta_ici)
sayı=[1,2,3,4,5]
hafta_ici.extend(sayı)#listeleri birleştirmek için kullanılır
print(hafta_ici)
hafta_ici.insert(2,"PAZARSALI")#listenin belirtilen noktasına eleman ekleme 
print(hafta_ici)
hafta_ici.remove("PAZARSALI")#listenin içinden değeri verilem elemanın siler
print(hafta_ici)
