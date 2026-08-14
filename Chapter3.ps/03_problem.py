# Problem based upon the string methods and functions
# 1. Take the string " i love python programming "  and:
"""1.Remove the extra spaces form both the ends
2. Convert it to title
3. Count how many times "o" appears"""

str="  i love python programming  " 
print(str.replace("  "," "))
print(str.strip()) # By using strip you can remove the unnecessary spaces in the string
print(str.title())
print(str.count("o"))

# Check if the string "123abc" is alphanumeric
string="123abc"
print(string.isalnum())