class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sum(self,p):
        return Point((self.x+p.x),(self.y+p.y))
    def print_Point(self):
        return(f"X is {self.x} and Y is {self.y}")
    # For overloading of the code we can do as follows
    def __add__(self,p): # This is used for overloading "+" attribute 
        return Point((self.x+p.x),(self.y+p.y))

p1=Point(3,2)
p2=Point(12,34)
# p=p1.sum(p2) Use when you don't use the __add__ attribute for overloading
p= p1 + p2
print(p.print_Point())