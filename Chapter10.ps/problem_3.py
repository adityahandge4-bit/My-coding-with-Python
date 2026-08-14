class Animal:
    location="England"
    def __init__(self,name,breed,location):
        self.name=name
        self.breed=breed
        self.location=location
    def Info_Animal(self):
        return(f"The name of Dog is {self.name},whereas the breed of the dog is {self.breed} and the dog is from {self.location}")
    def speak(self):
        print("The sound made by every dog is")
class Dog():
    def speak(self):
        return("Bhow Bhow")
Info=Animal("Cristopher","Labrodor Reteiver","Australia")
print(Info.Info_Animal())
Info.speak()
Info_2=Dog()
print(Info_2.speak())
    
    

# If you do not use a decorator you have to call the class a well as subclass




# Whenever you will make use of class and object method just remember one thing you always have to make use "self" always so that your class would be directed towards the object
    


