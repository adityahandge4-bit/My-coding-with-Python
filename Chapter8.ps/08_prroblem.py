# Write a python function to print multiplication table of a given number.
# By my method by using loops
# n=int(input("Enter the number:  "))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")

# By using functions
def table(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
table(10)
