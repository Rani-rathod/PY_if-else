n=input("enter the date:-")
a=n[0:2]
b=n[3:5]
c=n[6:]
if (int(c)%4==0) and a<="28" and b=="02":
    print(int(a)+1,"/",b,"/",c)
elif (int(c)%4==0) and a=="29":
    print("01/",int(b)+1,"/",c)
if (b=="01" or b=="03" or b=="05" or b=="07" or b=="09" or b=="10" or b=="12") and a<="30":
    print(int(a)+1,"/",b,"/",c)
elif (b=="01" or b=="03" or b=="05" or b=="07" or b=="09" or b=="10") and a=="31":
    print(b=="01/",int(b)+1,"/",c)
if (b=="04" or b=="06" or b=="08" or b=="11") and a<="29":
    print(int(a)+1,"/",b,"/",c)
elif (b=="04" or b=="06" or b=="08" or b=="11") and a<="30":
    print("01/",int(b)+1,"/",c)
if b=="12" and a=="31":
    print("01/01",int(c)+1)

