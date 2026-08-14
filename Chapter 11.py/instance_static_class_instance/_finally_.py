# try:
#     a=int(input("Enter the number 1:   "))
#     b=int(input("Enter the number 2:   "))
#     c=a/b
#     print(c)
# except Exception as e:
#     print(e)
# finally:
#     print("This occurs always")
# Why there is an importance of finally over here
def division_(a,b):
    try:
        c=a/b
        print(c)
        return c
    except Exception as e:
        print(e)
        return None
    # print("This always occur")  # Without make use of "finally" this will never print always or I would say, IT WILL NEVER PRINT
    finally:
        print("This always occur")
    
a=int(input("Enter the number 1:   "))
b=int(input("Enter the number 2:   "))
division_(a,b)
