# Write a recurssion function for printing the factorial of the specified number
def factorial(n):
    for i in range(1,n+1):
        if(n==0 or n==1):
            return 1
        return n*factorial(n-1)
n=int(input("Enter the value:  "))
print(f"The factrial of {n} is the {factorial(n)}")

# Write a recurssive function for sum of all digits
def sum_of_digits(n):
    for i in range(1,n+1):
        if(n==1):
            return 1
        return n+sum_of_digits(n-1)
n=int(input("Enter the value: "))
print(sum_of_digits(n))

# Bhai nehmi lakshat thevayche ki jevha recurssion ale tar lagech  1st part base condition dyaychi mhanje dyaychich
def sum_of_digits(n):
    if(n==0):
        return 0
    return n%10+sum_of_digits(n//10)
print(sum_of_digits(4567))








# def Sum_digits(n):
#     if n==0:
#         return 0
#     return n%10 + Sum_digits(n//10)
# print(Sum_digits(789))