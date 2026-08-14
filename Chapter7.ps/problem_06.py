#Write a program to calculate the factorial of a given number using for loop.


n=int(input("Enter the number:   "))
product=1
for i in range(1,n+1):
    product=product*i
print(f"The factorial of {n} is the {product}")
# If you go through normal way making use of for loop is very easy and quick functional
# On the other hand if you use a functions so the  point to be noted is that you have to make use of recurssions and state the base condition and then only the function and the code will become funcntional.

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)
print(factorial(3))












# For extra practise/practice
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n* factorial(n-1)
print(factorial(8))