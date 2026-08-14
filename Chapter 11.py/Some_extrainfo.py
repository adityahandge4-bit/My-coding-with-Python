def decorator(func):
    def wrapper():
        print("I am there to execute a program....")
        func()
        print("I have executed the program")
    return wrapper


@decorator   # This is a way of advanced python thus to make the variable to be under the decorator so that we can call it.
def say_hello():
    print("Hello!")

say_hello()