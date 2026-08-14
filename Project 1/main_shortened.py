# if(computer==you):
#     print("It's a draw")
# else:
#     if(computer==1 and you==0): 1
#         print("You lose!")
#     elif(computer==1 and you==-1): 2
#         print("You win!")
#     elif(computer==0 and you==1):-1
#         print("You win!")
#     elif(computer==0 and you==-1):1
#         print("You lose!")
#     elif(computer==-1 and you==1):-2
#         print("You lose!")
#     elif(computer==-1 and you==0):-1
#         print("You win!")
#     else:
#         print("Something went wrong")

import random
'''
Here,
snake=1
water=0
gun=-1'''
computer=random.choice([1,0,-1])
youstr=input("Enter your choice:  ")
youdict_={"s":1,"w":0,"g":-1}
reversedict_={1:"Snake",0:"Water",-1:"Gun"}
you=youdict_[youstr]

print(f"You chose {reversedict_[you]}\nComputer chose {reversedict_[computer]}")

if('computer-you=1' or 'computer-you=-2'):
    print("You lose!")
else:
    print("You win!")



# This is a shortcut way to make the game
    
