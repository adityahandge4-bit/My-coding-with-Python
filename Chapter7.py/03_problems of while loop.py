#Write a program to print the content of a list using while loops
list=["Harry","Suresh","Abhinav","Shailesh"]
i=0
while(i<4):
    print(list[i])
    i+=1
for i in range(0,4): # You can also make use of the for loops but the most important thing before using the for loop is that state the range of i otherwise it will run the error as "print(list[i])
#           ~~~~^^^
# TypeError: list indices must be integers or slices, not str"
# Hence also remember what kind of error can arise after running the wrong code.
    print(list[i])
    














