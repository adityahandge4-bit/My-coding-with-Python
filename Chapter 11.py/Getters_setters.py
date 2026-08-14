class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def first_name(self):
        l=self.name.split(" ")  # If I say split as this functionality we can make the list from it.
        print(l)
        return l[0]
e=Employee("Jack Doe",34000)
print(e.first_name())
# This all code were done for understanding the classes amd objects as in new way
# this above method is used to print the first name of the employee
  

# And if you want to change that any name location so you can use the following method
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def first_name(self):
        l=self.name.split(" ")  # If I say split as this functionality we can make the list from it.
        return l[0]
    def first_setter(self,first):
        l=self.name.split(" ") 
        new_name=f"{first} {l[1]}"
        self.name=new_name

    
e=Employee("Jack Doe",34000)
print(e.first_name())
e.first_setter("Harry")
print(e.name)
# print(e.first_name())


# Here we make use of the decorators inside the class object method 
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    @property  # By making use of this decorative we can access this kind of function at the location of the object
    def first_name(self):
        l=self.name.split(" ")  # If I say split as this functionality we can make the list from it.
        return l[0]
    
    @first_name.setter   # Same as we can accesss the function coming under this decorater
    def first_name(self,first):
        l=self.name.split(" ") 
        new_name=f"{first} {l[1]}"
        self.name=new_name

    
e=Employee("Jack Doe",34000)
print(e.first_name)
# e.first_setter("Harry")
# print(e.name)
e.first_name="John"
print(e.name)