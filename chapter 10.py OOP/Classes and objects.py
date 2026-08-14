# class is actually a blueprint or a template. It ddefines what an object be like and what data it holds and what actions it can perform.It works after instructing it in a specific way
# Class is like an architectural plan
  # Whereas object is building the real home from an arhitectural plan
# It is created from an instance from the classes


class Employee:
    company="HP"

    def get_salary(self):# self is important here because self is a way to reference the object of the class which is being created
        print(self)
        print( 340000)
e=Employee()# An object of class Employee is created here
e.get_salary() # Employee e's get salary method is called

# same result but under different variable
e2=Employee()
e2.get_salary()









# class company:
#     def get_salary(self):
#         return 890000
    
# e1=company
# print(e1.get_salary())