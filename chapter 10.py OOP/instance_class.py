class Employee:
    company="Asus"  # This is a class atribute
    def __init__(self,salary,name,bond,experience,company):
        self.salary=salary
        self.name=name
        self.bond=bond
        self.experience=experience
        self.company=company
    
    def get_salary(self):
        return self.salary
    def info_employee(self):
        return(f"The name of the employee is {self.name} . Salary of the employee is {self.salary}.The bond of the employee is {self.bond}.The experience of the employeee is {self.experience} years")
e=Employee(34000,"Arjun Das","4 years",23,"Mahindra")
print(e.company)   # This will print instance attribute whenever present
# Output will be Mahindra
print(e.name)
print(Employee.company) # If you make use of the class it will print the class atribute whereas in another rexample or code where you print(e.company) in this it will consider the instance attribute


# object interspection
# This method is used to find all the methods that come under class and that can be used while using class object method
print(dir(e))
