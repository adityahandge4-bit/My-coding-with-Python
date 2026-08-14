#Write a program to find whether a given number is prime or not
# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")

'''Take number
↓
If number ≤ 1
    Not prime
Else
    Check divisibility from 2 to √num
        If divisible
            Not prime
            Stop
    If no divisor found
        Prime'''  # summary of the problem

# For a program for printing whether the number is prime number or not
# For revision purpose
n=int(input("Enter the number: "))      
if n<=1:
    print("The number is not the prime number.")

else:
    for i in range(2,int(n*0.5)+1):
        if n % i==0:
            print("The number is not the prime number.")
            break

    else:
        print("The number is a prime number.")
        

  