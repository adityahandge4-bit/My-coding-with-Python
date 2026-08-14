# Make use of increament function as follows
def increament():
    counter=0
    counter+=1
    return counter
print(increament())
print(increament())
print(increament())
print(increament())
print(increament())
# It will change since the counter variavle is a local variable

# Write a function multiply(a,b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring
def multiply(a,b):
      """
    Multiply two numbers and return their product.

    Parameters:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        int | float: The product of a and b.

    Example:
        >>> multiply(4, 5)
        20
    """
      return a*b
print(multiply.__doc__)
help(multiply)



    


