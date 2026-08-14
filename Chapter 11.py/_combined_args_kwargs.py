def func(*args,**kwargs):
    print(args)
    print(kwargs)
func(1,2,34,56,78,Harish=890,Joseph=567,Harry=1000,Thalapathy=10000)
# The output of the above programe is
"""
(1, 2, 34, 56, 78)
{'Harish': 890, 'Joseph': 567, 'Harry': 1000, 'Thalapathy': 10000} 

"""
def sum(*args):
    print(args)
    total=0
    for items in args:
        total+=items
    return total
print(sum(12,23,45,67,78,90,964543))

def dic(**kwargs):
    print(kwargs)
    for items in kwargs:
        print(f"{items}:{kwargs[items]}")
dic(Harry="c++",Rohan="Python",Satish="Jawa",Manoj="C")