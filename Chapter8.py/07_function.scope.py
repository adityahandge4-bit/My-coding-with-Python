def sum(a,b):
    c=a+b
    return c
print(sum(56,78))

# Always remember that when yo write a certain function so python program will analyse it and then considered it as a temporary variables and then delete those variables
# Such a variables are called as local variables


def sum(a,b):
    c=a+b
    z=90  # This is a local variable
    return c
z=98    # This is a global variable
print(z) 
print(sum(56,78))


# If you print local variable,it will not print becaue python programme erase it as you return the value but python programme will print the global variable since it is defined.
def subtract(a,b):
    c=a-b
    global z    # this statement says to make the variable z as global variable
    z=1           # This will refer to global z and not create a local variable
    return c
print(subtract(100,1))
print(z)