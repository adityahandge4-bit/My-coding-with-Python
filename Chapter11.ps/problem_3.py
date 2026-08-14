# class Employee:
#     def __init__(self,salary):
#         self._salary=salary  # This is called a private attribute

#     @property
#     def salary(self):
#         return self._salary
    
#     @salary.setter
#     def salary(self,value):
#         if value<0:
#             print("Hey don't write the negative value of the salary")
#         else:
#             print(value)
# e=Employee(7899000)
# e.salary=-9000
# print(e.salary)


class Employee:
    def __init__(self,salary):
        self._salary=salary
    @property
    def salary(self):
        return self._salary
    @ salary.setter
    def salary(self,new_salary):
        if new_salary<0:
            print("Hey don't give the negative value")
        else:
            print(new_salary)
        # print(f"The salary of the employee is {new_salary}")
        # return self._salary==new_salary
a=Employee(7890)
a.salary=-85600
print(a.salary)












