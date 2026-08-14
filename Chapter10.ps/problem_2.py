# Create a class by using the constructer
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def personal_info(self):
        print(f"The name of person is {self.name} and the age of the person is {self.age}.")
info=person("Avinash",35)
info.personal_info()