# Write a program using functions to find greatest of three numbers.
def greatest(a,b,c):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a=int(input("Enter the number:  "))
b=int(input("Enter the number:  "))
c=int(input("Enter the number:  "))
print("The greatest of the all numbers is:",greatest(a,b,c))

