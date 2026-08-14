class Employee:
    def __init__(self,salary,name,bond,experience):
        self.salary=salary
        self.name=name
        self.bond=bond
        self.experience=experience
    
    def get_salary(self):
        return self.salary
    def info_employee(self):
        print(f"The name of the employee is {self.name} . Salary of the employee is {self.salary}.The bond of the employee is {self.bond}.The experience of the employeee is {self.experience} years")
e=Employee(34000,"Arjun Das","4 years",23)
e.info_employee()
print(e.get_salary())