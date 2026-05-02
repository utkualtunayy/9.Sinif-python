from datetime import datetime
bugun=datetime.today()
yıl=int(input("lütfen dogum yılı giriniz"))
ay=int(input("dogum ayı gir"))
gun=int(input("dogum günü gir"))
dogum=datetime(year=yıl,month=ay,day=gun)
yas=bugun-dogum
print("yasınız=",yas)
