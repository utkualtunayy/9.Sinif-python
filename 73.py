#soru
a=int(input("bir sayı giriniz:"))
yirmi=int(a/20)
klanyi=a%20
on=int(klanyi/10)
kon=on%10
bes=a-((yirmi*20)+(10*on))
besi=int(bes/5)
print("yirmi=",yirmi,"onluk=",on,"beslik=",besi)