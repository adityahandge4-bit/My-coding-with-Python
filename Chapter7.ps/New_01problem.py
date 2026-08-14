# Print numbers from 1 to 10 using for loops
# for i in range(1,11):
#     print(i)

# Print multiplication table of anumber according to the input given by the user
a=int(input("Enter the number: \n "))
for i in range(1,11):
    print(f"{a}x{i}={a*i}")
    # or
    print(a,"x",i,"=",a*i)

# Remember that if write as below you would get the table of only one digit because it is specifically assigned for that method only
i=1
for i in range(1,11):
    print("2x",i,"=",2*i)
    i+=1


# Calculate the sum of all numbers from 1 to 100 using for loop
n=int(input("Enter the number:  "))
sum=0
n=int(input("Enter the number:  "))
for i in range(1,n+1):
    sum+=i
print(sum)

