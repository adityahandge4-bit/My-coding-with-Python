'''
factorial by my method
'''
n=int(input("Enter the number:  "))
product=1
for i in range(1,n+1):
    product=product*i
print(f"factorial of {n} is {product}")

# By methods of functions
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n* factorial(n-1)
a=int(input("Enter the number:  "))
print(f"Factorial of {n} is : {factorial(n)}")


# Some best examples of the recurssion by fibonachi series
"""
0 1 1 2 3 5 8 13
# Some extra information that is in Fibonachi series we add always last two digits with each other and then print them as mentioned above
fib(0)=0
fib(1)=1
fib(2)=1
fib(3)=2
fib(4)=fib(3)+fib(2)
fib(n)=fib(n-1) + fib(n-2)"""

def fib(n):
    if(n==0 or n==1):
        return n
    return fib(n-1) + fib(n-2)
print(fib(4))
# Always remember that givng base function is necessary while using the recurssion

"""for fib(6)=
fib(5)+fib(4)
fib(2)+fib(3)+fib(5)"""
fib(0)+fib(1)+fib(3)+fib(5)
0+1+fib(1)+fib(2)+fib(5)
0+1+1+fib(1)+fib(0)+fib(3)+fib(4)
0+1+1+1+0+fib(3)+fib(4)
0+1+1+1+0+fib(1)+fib(2)+fib(3)+fib(2)
# thi pattern refers a recurssion