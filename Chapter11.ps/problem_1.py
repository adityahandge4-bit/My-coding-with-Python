# write a decorator logger
# def decorator():
#     def logger():
#         print("Function is being called")
#     logger()
# def say_hello():
#     print("Hello")
# say_hello()
# decorator()




def logger(func):
    def wrapper():
       print("Function is being called")
       func()
    return wrapper

@logger
def say_hello():
    print("Hello!")
say_hello()