#önemli ve zor çalış bu soruya

tercih=input("sinama ise (s) ye tiyatro ise (t) ye basınız")
durum=input("öğrenci ise (ö) sivil ise (s) bilgisini giriniz")
if tercih=="s":
    if durum=="s":
        print("15tl")
    else:
        para=15-15*0.5
        print(para," tl")
else:
    if durum=="s":
        print("10tl")
    else:
        para1=10-10*0.5
        print(para1," tl")
