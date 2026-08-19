# Collection which is immutable is called Tuples
a=("Sakshi", "Anu", "Srinidhi", "Tripti")
print(type(a))

# Tuple with only single element
b=(67,)
print(type(b))
# Tuples are ordered but immutable
tuple_=(90,67,23,"Harry") # Here we can use of string slicing.
print(type(tuple_))
print(tuple_[3])  # This will print the 3rd character inside the tuple "tuple_"
print(tuple_[0:2:1])  # this method is use for  slicing inside the tuple.
print(tuple_[0:]) # Used for listing every term inside the tuple_ variable
print(tuple_[::-1]) # Used for listing every term inside the tuple_ variable in reverse pattern
