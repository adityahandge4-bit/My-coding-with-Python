# Bonus question
# Write a program that counts how many vowels are in a given string
string="Prathamesh Vikram Katkade"
sum=0
vowels=['a','e','i','o','u']
for char in string.lower():
    if(char in vowels):
        sum+=1
print(f"The vowels in the given string is {sum}")


# Take a input string and check if it is a palindrome(same forward and backward)
a=input("Enter the string:  ")
b=a.lower()
if(b[0::]==b[::-1]):
    print("The given string is a palindrome")
else:
    print("The string shows absence of palindrome")














# str="Aditya Sandeep Handge"
# sum=0
# vowels=["a","e","i","o","u"]
# for char in str.lower():
#     if(char in vowels ):
#         sum+=1
# print(f"Total number of the vowel are {sum}")