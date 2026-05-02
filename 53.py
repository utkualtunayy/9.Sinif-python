#fonksiyonla sistem toplama
def sistemtop():
 
 a=int(input("kasanın fiyatını giriniz:"))
 b=int(input("monütör fiyatını giriniz:"))
 c=int(input("klavye fiyatını giriniz:"))
 d=int(input("mause fiyatını giriniz:"))
 e=int(input("mause pad fiyatını giriniz:"))
 f=int(input("kulaklık fiyatını giriniz:"))
 cu=a+b+c+d+e+f
 print("---------------------------------------")
 print("sistemin toplam fiyatı:",cu)
 ayu=(cu/18000)
 print("bu sistemi toplamak için askeri ücretle",ayu,"ay çalışmalısın")
sistemtop()