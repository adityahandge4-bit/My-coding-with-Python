# For making a custom error you have to make the class
class NegativeNumberError(Exception):
    pass
try:
    
    num2=int(input("Enter the number:  "))
    c=35/num2
    if num2<0:
        raise NegativeNumberError
    print(c)
except ValueError:
    print("Hey put the number correct value other than that")
except ZeroDivisionError:
    print("Hey don't divide by zero")
except NegativeNumberError:
    print(f"Error:Hey don't write the negative number,")

# To raise the error with normal way





    


