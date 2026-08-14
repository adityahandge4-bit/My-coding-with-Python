# Decorator is a function which takes the function, it creates a new function inside its body(wrapper). Then it returns that new function
def decorator(func):
    def wrapper():
        print("I am there to execute a program....")
        func()
        print("I have executed the program")
    return wrapper
def say_hello():
    print("Hello!")
f=decorator(say_hello)
f()


"""
f will look something like this
def f():
    print("I am there to execute a program....")
    print("Hello!")
    print("I have executed the program")
    
    
    
    """  # This is the ouyput of the above mentioned program