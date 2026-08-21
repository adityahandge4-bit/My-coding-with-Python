# Print numbers from 1 to 100 uing a while loop
i=1
while(i<101):
    print(i)
    i+=1

# Write a program that keeps asking the user to enter a password until they enter the correct one


correct_password = "python123"

while True:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Access Granted!")
        break
    else:
        print("Incorrect password. Try again.")

# Use a while loop to reverse a given number
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)

# Or
# Simple method is what you can do string slicing
# as follows
a=int(input("Enter the number:  "))
print((str(a)[::-1]))

        

















# Mla jar number la reverse pattern madhye lihayche asel
number=int(input("Enter the number:  "))
print(int(str(number)[::-1]))