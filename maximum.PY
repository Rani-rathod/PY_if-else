var1=int(input("enter the first number:-"))
var2=int(input("enter the second number:-"))
var3=int(input("enter the therd number:-"))
if var1<var2 and var1>var3:
    print(var1,"var1 is gretor")
elif var2<var3 and var2>var1:
    print(var2,"var2 is gretor")
elif var3<var1 and var3>var2:
    print(var3,"var3 is gretor")
else:
    print("Both are equal")

