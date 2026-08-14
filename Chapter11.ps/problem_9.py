# def sum_all(*args):
#     total=0
#     for items in args:
#         total+=items
#     return total
# print(sum_all(23,45,67,8,9,9,7,6,5,44,3,3,3))

# def print_details(**kwargs):
#     print(kwargs)
# print_details(name="Alice",age=25,city="Delhi")


# # Another methods for kwargs
# def print_details(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# print_details(name="Alice",age=25,city="Delhi")











def sum_all(*args):
    total=0
    for items in args:
        total+=items
    return total
print(sum_all(89,90,876,54,21,32,90,99)) 

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_details(Harry="C++",Joseph="Python")