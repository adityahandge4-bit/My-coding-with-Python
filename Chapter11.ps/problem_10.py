# Bonus Challenges
def wrapper(*args,**kwargs):
    print(args)
    print(kwargs)
wrapper(23,23,45,67,89,Harry="Python",Joshi="Gate",Ghayal="Chemistry")


class Vector:
    def __init__(self):
        pass
    def __add__(self,a,b):
        print(a+b)
a=Vector
a.__add__(sum,12,34)

import logging

# Configure logging
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom Exception
class InvalidAgeError(Exception):
    pass

# Program
while True:
    try:
        age = int(input("Enter your age (or -1 to exit): "))

        if age == -1:
            print("Program ended.")
            break

        if age < 0 or age > 120:
            raise InvalidAgeError("Age must be between 0 and 120.")

        print("Valid age entered:", age)

    except ValueError:
        print("Invalid input! Please enter a number.")
        logging.error("ValueError: User entered a non-numeric value.")

    except InvalidAgeError as e:
        print("Custom Exception:", e)
        logging.error(f"InvalidAgeError: {e}")

    print("Program continues...\n")


    







    