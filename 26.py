bir=int(input("birinci kenarı giriniz"))
iki=int(input("ikinci kenarı giriniz"))
uc=int(input("ucuncu kenarı giriniz"))
if(bir==iki & iki==uc):
    print("eşkenar üçgen")
elif (bir==iki or iki==uc or bir==uc):
    print("ikizkenar")
else:
    print("çeşitkenar")