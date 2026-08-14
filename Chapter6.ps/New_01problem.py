# Write a program that ask a user for a number and prints whether it is positive, neagative or zero
a=int(input("Enter the number:  "))
if(a>0):
    print("The number is positive")
elif(a==0):
    print("The number is zero")
else:
    print("The number is negative")

# Create a program for a person is eligible for a vote or not

b=int(input("Enter the age:  ")) 
if(b>=18):
    print("You are eligible to vote")
elif(b<18):
    print("You are not eligible to vote")
else:
    print("You write a wrong input")

# Write a program for taking input from the user to check whether the number is even or odd

c=int(input("Enter the number:  "))
if(c%2==0):
    print("The number is even")
else:
    print("The number is odd")

