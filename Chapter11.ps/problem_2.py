# from time import time
# def timer(func):
#     def function(n):
#         t1=time()
#         result=func(n)  # To print the term present inside the decorator you can simply write the function inside the variable and then call it along with decorating the another function
#         t2=time()
#         print(t2-t1)
#         return result
#     return function
# @timer
# def sum_(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return(sum)
# print(sum_(1000000)) # Here you we can use a simple method the method we use regurarly and it will work easily but because of use of decorator we can't make use of it and hence in order to make the decoartor function to work we do not have to call the program but by just putting it inside the variable we make it non functional

# Or method
from time import time
def timercal_(func):
    def wrapper():
       t1=time()   
       t2=time()
       print(t2-t1)
       result=func()
       return result
    return wrapper
@ timercal_
def sum():
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(sum)
n=int(input("Enter the number: "))
sum()


    


