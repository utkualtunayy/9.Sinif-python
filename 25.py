k1=float(input("kilo giriniz")) #kullanıcıdan veri alma işlemi
if k1 < 20:
 print("valizinizin kilosu",k1,"olduğu için ücret ödemene gerek yok")
else:
   ucret=(int(k1)-20)*10
   print("ek ücret",ucret)
