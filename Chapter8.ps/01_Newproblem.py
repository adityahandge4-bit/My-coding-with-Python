# Write a function for greeting the learner a Hello python learner
def greet(name):
    print(f"Hello {name}, the keen python learner",sep=",")
greet("Harry")

# Write a function for squaring the number 
# def square(num):
#     c=num**2
#     return c
# print(square(23))
# Other way
def square():
    a=lambda m: m**2
    print(a(12))
square()