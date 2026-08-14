# Ask the user to enter the day number (1-7) and print the corresponding day pf the week using match case

# num=int(input("Enter the number:  "))

# match(num):
#     case 1:
#         print("The day is Sunday")
#     case 2:
#         print("The day is Monday")
#     case 3:
#         print("The day is Tuesday")
#     case 4:
#         print("The day is Wednesday")
#     case 5:
#         print("The day is Thursday")
#     case 6:
#         print("The day is Friday")
#     case 7:
#         print("The day is Saturday")
#     case _:
#         print("You enter the invalid number")



# Write a program to simuulate a simple calculator








# to design a simple calculator
a=int(input("Enter the value:  "))
b=int(input("Enter the value:  "))
operation=input("Enter the operation:  ")
match operation:
    case"+":
        print(a+b)
    case"-":
        print(a-b)
    case"*":
        print(a*b)
    case"/":
        print(a/b)