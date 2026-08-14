class Birds:
    def __init__(self,name,country):
        self.name=name
        self.country=country
Birds_=Birds("Maldhock","India")
print(Birds_.name)
print(Birds_.country)









class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def speak():
        return("The common sound make by the Animal is as follows")
        
class Dog(Animal):
    def speak():
        return "Bark"

e=Animal("Bruno","Labrador Reteiver")
print(e.name)
print(e.species)
print(Animal.speak())
print(Dog.speak())