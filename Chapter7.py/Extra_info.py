# For printing the table of any number
# You can also do it

# for i in range (1,11):
#     print("5x",i,"=",5*i)
#     print(f"5x{i}={5*i}")
# You have both ways for writing table of any number
# Remember that if you use the comma an automatic space is created between the code you have written
i=1
n=int(input("Enter the number: "))
while(i<=10):
    print(f"{n}x{i}={n*i}")
    i+=1

# You can also make use of for loop
num=int(input("Enter the number: "))
for i in range(1,11):
    print(f"{num}x{i}={num*i}")
