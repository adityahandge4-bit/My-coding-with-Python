# write the program for writing the full name of certain person
def full_name(first,last):
    c=f"Let me introduce \"{first} {last}\""
    return c
print(full_name("Aditya","Handge"))

# Write a python programme that call for the area of rectangle
def calculate_area(length,width):
    c=f"Area of rectangle is:{length*width}"
    return c
print(calculate_area(56,78))
# Here we use length and width with unknown values but now with default value as below
def calculate_area(length,width=89):
    c=f"Area of rectangle is:{length*width}"
    return c
print(calculate_area(12,))
# To be noted if a crtain value is given in default then you don't have to once again write that specific value once again while ending the function