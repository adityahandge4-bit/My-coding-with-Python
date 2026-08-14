class Animal:
    location="Australia"
    def __init__(self,name):
        self.name=name
    def speak(self):
        return(f"Generic animal sound of {self.name} is as follows:")
class dog(Animal):     # This actually being used to take a subclass uder the origial class Animal. Whereas always remember this method.
    def speak(self):   # This way is actually being used to make the python programme to speak out the fuction that comes under the class
        super().speak()
        print("BhowBhow")
d=Animal("Bruno") # I want to consider the class of the dog hence I take variable d to assign and direct the class towards the object variable that I want to print.
print(d.location)
print(d.speak())
# print(d.location) # As the class dog comes under the superclass Animal so you can use the lower class thus to get the orientations inside the superclass
d=dog("Bruno")
d.speak()
# The method to comment the existing class attribute and to call it.