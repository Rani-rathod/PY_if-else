
# num=int(input("enter the number:-"))
# a=num%10
# b=(num//10)%10
# c=(num//100)%10
# d=(num//1000)%10
# number=(a*1000)+(b*100)+(c*10)+(d*1)
# if number:
#     print(number)






user_name=input("enter the upper case:-")
if user_name>="A" and user_name<="Z":
    print("its a upper case")
    lower_case=input("enter the lower case:-")
    if lower_case>="a" and lower_case<="z":
        print("its lower case")
        special_char=input("enter the special char:-")
        if special_char=="@" or  special_char=="#" or special_char=="$":
           print("its a special char")
           numeric=input("enter the numeric:-")
           if numeric>="0" and numeric<="9":
              print("it is a numeric")
              a=(user_name+lower_case+special_char+str(numeric))
              if len(a)==8:
                   print("it is strong passward",a)
              else:
                   print("")
           else:
                print("")
        else:
            print("")
    else:
        print("")
else:
    print("")                               


               

    