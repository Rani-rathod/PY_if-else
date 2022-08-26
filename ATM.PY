print("welcome to ATM")
card=input("enter your card:-")
if card=="credeit card" or "debit":
    print("take")
    lang=input("enter the language:-")
    if lang==" hindi" or "english":
        print("Okay this language")
        num=int(input("enter the 4 digit no :-"))
        if num<=1 or num>=10:
            print("select")
            accound=input("enter the accound:-")
            if accound=="saving" or "curret":
                print("in proses")
                withdraw=int(input("enter the amount your want to withdraw:-"))
                if withdraw<=40000:
                    print("withdraw amount:" ,withdraw)
                    print("new amount :", 40000-withdraw)
                    recipt=input("enter the cash:-")
                    if recipt=="yes" or "no":
                        print("Ok take your money")
                    else:
                        print("not cash")
                else:
                    print("error")
            else:
                print("zero")
        else:
            print("not")
    else:
        print("type")
else:
    print("not card")



# print("Welcome to ATM")
# total_balance=500000
# atm=input("enter the card:-")
# if atm=="credit card" or atm=="debit card":
#     print("after")
#     language=input("please enter your language:-")
#     if language=="english" or language=="hindi":
#         print("english")
#         pin=int(input("enter the pin:-"))
#         if pin>=0 or pin<=9:
#             print("ok")
#             type=input("enter the type:-")
#             if type=="current" or type=="saving":
#                 print("in proese")
#                 trancsection=input("enter the trancsection:-")
#                 if trancsection=="withdrawal" or trancsection=="balance enquiry":
#                     print("okay")
#                     balance=int(input("enter the balance:-"))
#                     if balance>=0 or balance<=500000:
#                         print("go next")
#                         if total_balance%100==0:
#                             print(total_balance-balance)
#                             recipt=input("enter do you have recipt:-")
#                             if recipt=="yes":
#                                 print("next")
#                                 aym=input("take your atm banck:-")
#                                 if atm=="yes":
#                                     print("ok thank you")
#                                 else:
#                                     print("no")
#                             else:
#                                 print("nothing")
#                         else:
#                             print("anything")
#                     else:
#                         print("never")
#                 else:
#                     print("nooooo")
#             else:
#                 print("noo")
#     elif language=="hindi":
#         pin=int(input("apne 4 anko ka pin dala:-"))
#         if pin>=0 or pin<=9:
#             print("ha")
#             khata=input("apna khata ka parkar dale:-")
#             if type=="chalu" or "bachat":
#                 print("prakriya")
#                 trancsection=input("apne len den ka prksr chone:-")
#                 if trancsection=="nikashi" or trancsection=="blence ki puch tach kare":
#                     print("ok")

