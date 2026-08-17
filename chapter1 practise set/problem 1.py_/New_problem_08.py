# Operator Challenge
"""Write a program that:
1. Takes a input from the user
2. Print the square and cube of that number."""
def square(a):
    return a**2
square(23)

def square(n):
    return n**2
num=[12,34,45,3,45,67,89,98,99]
print(list(map(square,num)))
