class company:
    def __init__(self,name,experience,salary):
        self.name=name
        self.experience=experience
        self.salary=salary
        
    

    def __str__(self):     # This dunder is used by the user as fellow programmer
        return f"The name of the employee is {self.name} and the experience of the employee is {self.experience} and the salary of the employee is {self.salary}"
    
    def __repr__(self):     # This is used for the developer
        return f"The name of the employee is {self.name} and the experience of the employee is {self.experience} and the salary of the employee is {self.salary}"
    
    def __len__(self):   # use for finding the length of the the attribute
        return len(self.name)
    
e=company("Rohit",45,4500000)
print(e.name,e.experience,e.salary)
print(e.__str__())
print(e.__repr__())
print(e.__len__())


    