# # print a list containing the table of 5
# table=[]
# for i in range(1,11):
#     table.append(5*i)
# print(table)

# # Using the single line code for printing the table of 5 inside the list
# table=[5*i for i in range(1,11)]
# print(table)












n=int(input("Enter the number: "))
table_=[]
for i in range(1,11):
    table_.append(n*i)
print(table_)