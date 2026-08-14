class Book:
    def __init__(self,title,author):
        self.title=title # This is an attribute
        self.author=author # This is an attribute
    
    def __str__(self):
        print(f"The title of the book is {self.title}")

    def __len__(self):
        return len(self.title)
Book1=Book("The Cheery Tree","Ruskin Bond")
Book2=Book("Toxic","Yash")
Book1.__str__()
print(Book2.__len__())