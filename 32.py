boy=int(input("boynuzu giriniz"))
kilo=int(input("kilo giriniz"))
vki=(boy*boy)/kilo
if vki<=25:
    print("normalsın")
elif vki<=30:
    print("kilolusun")
else:
    print("obezsin")
    