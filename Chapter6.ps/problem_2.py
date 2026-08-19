# #Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# # input from the user.

# Program to check whether a student has passed or failed

sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

# Calculate total percentage
total_percentage = (sub1 + sub2 + sub3) / 3

# Check pass/fail conditions
if(total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("Student has Passed")
else:
    print("Student has Failed")

print("Percentage:", total_percentage)          

