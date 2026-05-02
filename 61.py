#hazır fonksiyon

from datetime import datetime
bugun=datetime.today() #başröl
print("bugün",bugun)
print(bugun.weekday()+1)
print("---------------------------------")
print("yıl=",bugun.year)
print("----------------------------------")
print("ay=",bugun.month)
print("----------------------------------")
print("saat=",bugun.hour)
print("----------------------------------")
print("dakika=",bugun.minute)
print("----------------------------------")
print("gün=",bugun.day)