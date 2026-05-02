#sürücü oldum dostum 

yas=int(input("yas giriniz"))
if yas<40:
    belge=input("sürücü belgen varmı (e/h)")
    üniversite=input("üniversite okudunmu (e/h)")
    if belge=="e" and üniversite=="e":
        print("hayırlı olsun işe alındın aylık 80 bin alıcaksın dostum")
    else:
        print("GİT senden olmaz")
else:
    print("fazla büyüksün")