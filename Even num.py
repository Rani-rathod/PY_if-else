# num=int(input("enter the number:-"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")


num=int(input("enter the num:-"))
i=1
a=0
while i<=num:
    if i%2==0:
        a=a+1
    i=i+1    
if a==2:
    print(num,"it is a prime number")
else:
    print(num,"it is not a prime number")            

