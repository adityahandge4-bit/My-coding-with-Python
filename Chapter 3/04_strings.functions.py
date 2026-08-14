#To find the length of the given syntex

name="Harry"
print(len(name))
#To find the exact way how a word starts or ends
print(name.endswith("rry"))
print(name.startswith("Ha"))
print(name.capitalize())

# How to make use of cpitalize fuction of string
name=("harry")
print(name.capitalize())

# How to use count function of string
name="Harry"
count= name.count("c")
print(count)
print(name.count('r'))

# How to use string.find word
name="Aditya"
index=name.find("itya")
print(index)

#How to use string fuction to replace certain word
name="Hello world"
replaced_string=name.replace("world","Dad")
print (replaced_string)
print(name.upper())