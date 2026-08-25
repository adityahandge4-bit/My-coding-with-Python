a=int(input("Enter the number 1:   "))
b=int(input("Enter the number 2:    "))
print(a+b)
# The above method is very kid type of code but if you want to get the code with a clear code
# follow as follows
while True:
    try:
        a=int(input("Enter the number 1:   "))
        b=int(input("Enter the number 2:   "))
        print(a/b)
    
    except  ValueError:
        print("Hey write the proper typecast")

    except ZeroDivisionError:
        print("Hey don't divide by the zero")

    except Exception as e:
        print(f"There's something error{e}")
  

# c=int(input("Enter the number 1:   "))
# d=int(input("Enter the number 2:   "))
# print(c/d)

# if d==0:
#     raise ValueError("Please don't divide by zero")
# print(f"The division is{c/d}")
# Sometimes we have to stop a devloper for writing the improper code so we can generally stop our own program like above mentioned method

# To be known errors are generally of varied type so thus to resolve it we just try to resolve those errors if there is a value error or there is tycasting error



"""By this way if in certain cases if the user is naughty and want to disturb the program so because of his mistake the programe will not end it will still go on continuation """