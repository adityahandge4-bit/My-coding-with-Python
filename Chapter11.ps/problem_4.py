class Mathutils:
    def __init__(self):
        pass
    
    
    @staticmethod
    def add(a,b):
        return f"sum of the both numbers is {a+b}"
    
    
    @classmethod
    def description(cls):
        print("This is a utility class for math operation.")
a=Mathutils
print(a.add(123,345))
a.description()
# print(Mathutils.add(123,345))
# Mathutils.description()

