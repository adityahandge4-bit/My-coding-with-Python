class Animal:
    location="Australia"
    def __init__(self,name):
        self.name=name
    def speak(self):
        return("Speaking now...... ")
class dog(Animal):
    def speak(self):
        super().speak()
        print("BhowBhow")
a=Animal("Bruno")
print(a.speak())
e=dog("Animal")
e.speak()
print(e.location) # Always remember that the string object is not callable
