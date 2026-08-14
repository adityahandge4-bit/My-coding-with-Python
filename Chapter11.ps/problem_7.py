# Making use of map
# a=[1,2,3,4,5]

# print(list(map(lambda x:x**3,a)))

# # Making use of filter
# num=[10,11,12,13,14]
# num_filter=list(filter(lambda x:x%2==0,num))
# print(num_filter)
# # Making use of reduce
# from functools import reduce
# lis=[1,2,3,4]
# lis_reduce=reduce(lambda x,y:x*y,lis)
# print(lis_reduce)


# Without using lambda
# For mapping
numbers=[1,2,3,45,6,7]
def cube(x):
    return x**3
print(list(map(cube,numbers)))
# For filtering
def numbers(num):
    return num%2==0
n=[1,2,3,4,5,67,8]
new_list=list(filter(numbers,n))
print(new_list)
# making use of reduce
from functools import reduce
def multiply(x,y):
    return x*y
numbers=[12,23,4,5,6,7]
print(reduce(multiply,numbers))
    