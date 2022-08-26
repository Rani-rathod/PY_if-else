


print("welcame to gmail")
name=input("enter the first name:-")
if name>="a" and name<="z" or name>="A" and name<="Z":
    print("Okay Next")
    name=input("enter the last name:-")
    if name>="a" and name<="z" or name>="A" and name<="Z":
        print("write")
        date=int(input("enter the date:-"))
        if date>=1 and date<=31:
            print("now enter the month")
            month=int(input("enter the month:-"))
            if month>=1 and month<=12:
                print("now enter the year")
                year=int(input("enter the year:-"))
                if year>=0 and year<=2021:
                    print(date,"/", month,"/",year)
                    gender=input("enter the gender:-")
                    if gender=="female" or "male":
                        print("custom")
                        password=int(input("enter the password:-"))
                        if password>=0 or password<=100:
                            print("create password")
                            mobile_number=int(input("enter the phone number:-"))
                            if mobile_number>=1 or mobile_number<=100:
                                print("more options")
                                email_id=input("enter the email_id:-")
                                if email_id=="ranirathod20@navgurukul.org":
                                    print("thanks you")
                                else:
                                    print("sorry")
                            else:
                                print("error")
                        else:
                            print("wrong")
                    else:
                        print("not")
                else:
                    print("not write")
            else:
                print("wrong")
        else:
            print("error")
    else:
        print("wrong name")
else:
    print("error")

