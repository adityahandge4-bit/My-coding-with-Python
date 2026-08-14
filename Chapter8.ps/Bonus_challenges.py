#  Write a recursive function fibonacci(n) that prints the first fibonacci numbers
def fibonacci(n):
    if(n==0 or n==1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(8))
"""0,1,1,2,3,5,8,13,21"""

# Write a function safe_divide(a,b) that returns the result of a/b, but returns "Cannot divide by zero" if b =0
def safe_divide(a,b):
    if(b==0):
        print("Cannot divide by zero")
    else:
        return a/b
print(safe_divide(78,2))



