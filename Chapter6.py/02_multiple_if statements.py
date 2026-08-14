a=int(input("Enter your age:  "))
# Multiple if statements

if(a%2==0):
    print("a is even") 
    
if(a>18): 
    print("Your age is above the age of consent")
 

elif(a<0):
    print("Negative age is not possible")

elif(a==0):
    print("Age is 0 is invalid age")

else:
    print("Your age is applicable for the consent")

print("End of program")
