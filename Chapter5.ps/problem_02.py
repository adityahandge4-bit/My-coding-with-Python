# Write a program to input eight numbers from the user and display all the unique numbers
# (once)
# a=set()
# for i in range(8):
#     no_=int(input(f"Enter the number {i+1}:  "))
#     a.add(no_)
# print(a)

















a=set()
for i in range(0,8):
    numbers=int(input(f"Enter the numbers{i+1}: "))
    a.add(numbers)
print(a)


