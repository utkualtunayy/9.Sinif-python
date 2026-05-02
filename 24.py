a1=int(input("açı giriniz")) #kullanıcıdan veri alma işlemi
a2=int(input("açı giriniz")) #kullanıcıdan veri alma işlemi
a3=int(input("açı giriniz")) #kullanıcıdan veri alma işlemi

# açı hesaplamak için gerekli kodlar
top=(a1+a2+a3)
if top == 180:
   print("açılarınızın toplamı",top,"olduğundan dolayı bu bir üçgendir")
else:
    print("açılarınızın toplamı",top,"olduğundan dolayı bun üçgen değidir")