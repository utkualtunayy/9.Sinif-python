s1=float(input("sınav notunuzu giriniz"))
s2=float(input("sınav notunuzu giriniz"))
ort=(s1+s2)/2
if ort<50:
    print("uzattın")
elif ort<60:
    print("kaldın")
else:
    print("geçtin")
   