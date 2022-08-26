

num=input("enter the facebook:-")
if num=="singup":
    print("welcome to facebook")
    name=input("enter the first name:-")
    if name>="a" and name<="z" or name>="A" and name<="Z":
        print("next")
        name=input("enter the last name:-")
        if name==name>="a" and name<="z" or name>="A" and name<="Z":
            print("write")
            date=int(input("enter the date:"))
            if date>=1 and date<=31 :
                print(" now enter the month")
                month=int(input("enter the month:"))
                if month>=1 and month<=12:
                    print("now enter the year")
                    year=int(input('enter the year:'))
                    if year>=0 and year<=2021:
                        print(date ,"/",month,"/",year)
                gender=input("enter the gender:-")
                if gender=="female" or "male":
                    print("custom")
                    mobile_number=int(input("enter your phone number:-"))
                    if mobile_number>=0 or mobile_number<=100:
                        print("write number")
                        password=int(input("enter choose a 4 passward:-"))
                        if password>=0 or password<=100:
                            print(password,"currect")
                            id=input("enter the email id:-")
                            if id=="ranirathod20@navgurukul.org":
                                print("careat")
                            else:
                                print("not careat")
                        else:
                            print("plese chek")
                    else:
                        print("error")
                else:
                    print("wrong")
            else:
                print("wrong")
        else:
            print("name is not")
    else:
        print("not write")
else:
    print("login") 





# id="ranirathod20@navgurukul.org"
# password=5821
# print("welcome to facebook")
# name=input("enter your id")
# if name==id:
#     print("ranirathod20@navgurukul.org")
#     pwd=int(input("enter your password"))
#     if pwd == password:
#         print("login succesfull")
#     else:
#         print("in correst password")
# else:
#     print("wrong id")



    


