# To write the python programme for comparison operator

a=34
b=80
c=(a>b)
print(c)

# Making use of input fuction for above programming
try:
    def compare():
        a=int(input("Enter number a is "))
        b=int(input("Enter number b is "))
        if a>b:
            print(f"{a} is greater than {b}",a>b)
        elif a==b:
            print(f"{a} is equal to {b}",a==b)
        elif a<b:
            print(f"{b} is greater than {a}",a<b)
    compare()
except ValueError:
    print(f"Write the correct value.")
# More advance way of making use of input functionality.
