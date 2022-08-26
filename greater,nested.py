num1=int(input("enter the greater:-"))
num2=int(input("enter the greater:-"))
num3=int(input("enter the greater:-"))
if num1>num2:
    if num1>num3:
        print(num1,"is greater")
if num2>num1:
    if num2>num3:
        print(num2,"is greater")
if num3>num1:
    if num3>num2:
        print(num3,"is greater")
else:
    print("equal")