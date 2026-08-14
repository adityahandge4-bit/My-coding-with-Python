from functools import reduce

numbers=[1,23,99,100,34,567]
    #=[24,99,100,34,567] In every step the reduce function add the elements present inside the list.
    #=[123,100,34,567]
    #=[223,34,567]
    #=[257,567]
    #=[824] Like how reduce works
def sum(a,b):
    return a+b
c=reduce(sum,numbers)
print(c)