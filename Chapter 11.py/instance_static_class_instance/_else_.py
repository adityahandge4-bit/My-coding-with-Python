try:
    a=34/10

except Exception as e:
    print("This is an error",e)
    print(e)# But if you don't want your program to be ended we can make use of the following method

else:
    print("Hey I am good!") # To be noted this will not run untill the error is not resolved
