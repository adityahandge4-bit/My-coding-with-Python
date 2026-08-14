# Making use of the filters methods
# def num_greater(x):
#     if x>9:
#         return True
#     else:
#         return False
# a=[12,23,45,6,7,8,9,34,5,6,233,45,56677,1234445]
# new=list(filter(num_greater,a))
# print(new)


















def modify(n):
    if n>9:
        return True
    else:
        return False
n=[122,3,4,5,66,7,79,8,1223,45,67,9,90]
new_num=list(filter(modify,n))
print(new_num)