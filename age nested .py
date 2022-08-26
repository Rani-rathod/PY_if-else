# age=int(input("enter the age:-"))
# if age>5:
#     print("you can go to school")
#     if age>=18:
#         print("you can vote in elections")
#         if age>=21:
#             print("you can drive a car")
#             if age>=24:
#                 print("you can marry")
#             else:
#                 print("invilet")
#         else:
#             print("error")
#     else:
#         print("not")
# else:
#     print("you can not go to school")





age=int(input("enter the age:-"))
if age>=18:
    collage=input("collage jata hai ya nhi:-")
    if collage=="yes":
        name=input("which collage:-")
        field=input("which field do you study:-")
        if field=="science":
            print("1 sal me job milegi")
        elif field=="math":
            print("1.50 me job milegi")
        elif field=="art":
            print("2 sal me job milegi")
    elif collage=="no":
        married=input("are you married:-")
        if married=="yes":
            type=input("which marrage:-")
            if type=="arrange":
                print("happy wedding")
            elif type=="love":
                place=input("where do you get marrage:-")
                if place=="temple":
                    print("god bless you")
                elif place=="court":
                    print("friend circle")
        elif married=="no":
            print("enjoy your self")
elif age<18:
    school=input("school jate ho ya nhi:-")
    if school=="yes":
        subject=input("which subject:-")
        if subject=="science" or subject=="math":
            print("it is nice field")
    elif school=="no":
        print("do your study")
else:
    print("invalid")

