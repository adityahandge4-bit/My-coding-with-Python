# Problrm to accept marks of 6 students and display in sorted manner

# marks=[]
# f1=int(input("Enter your marks here: "))
# marks.append(f1)
# f2=int(input("Enter your marks here: "))
# marks.append(f2)
# f3=int(input("Enter your marks here: "))
# marks.append(f3)
# f4=int(input("Enter your marks here: "))
# f5=int(input("Enter your marks here: "))
# marks.append(f5)
# f6=int(input("Enter your marks here: "))
# marks.append(f6)
# f7=int(input("Enter your marks here: "))
# marks.append(f7)
# marks.sort()
# print(marks)




marks=[]

for i in range(6):
    mark=input(f"Enter the marks {i+1}: ")
    marks.append(mark)
    marks.sort()
print("Sorted marks are: ", marks)




