
s1=int(input("Birinci sınav notu giriniz")) #kullanıcıdan veri alma işlemi
s2=int(input("İkinci sınav notu giriniz")) #kullanıcıdan veri alma işlemi
p3=int(input("performans notu giriniz")) #kullanıcıdan veri alma işlemi
p4=int(input("performans notu giriniz")) #kullanıcıdan veri alma işlemi

# ortalama hesaplamak için gerekli kodlar
ortalama=(s1+s2+p3+p4)/4
if ortalama<50:
    print("ortalamanız ",ortalama,"olduğundan kaldınız")
else:
       print("ortalamanız ",ortalama,"olduğundan geçtiniz")