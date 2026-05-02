#offff 
def fonk():
    a=int(input("bir sayı giriniz:"))
    b=int(input("bir sayı giriniz:"))
    c=input("bir işaret giriniz:(/)(+)(*)(-):")
    if c=="+":
        print(a+b)
    if c=="-":
        print(a-b)
    if c=="/":
        print(a/b)
    if c=="*":
        print(a*b)

fonk()