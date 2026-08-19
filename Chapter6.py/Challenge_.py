# Write a program to print yes when the age entered by the user is greater than or equal to 18.

age=int(input("Enter your age:  "))

if(age>=18):
    print("yes")

elif(age<18):
    print("No! you are not eligible")

elif(age==0):
    print("Age can't be zero,give the correct age")

elif(age<0):
    print("Age cannot be negative")

else:
    print("You have not given correct syntax")
    
print("End of program")    