# Write a program to make a copy of a text file “this.txt”.
with open("this.txt1","r") as f:
    text=f.read()

with open("this.txt copy","w") as  f:
    f.write(text)

import os

print(os.getcwd())

with open("myfile.txt", "w") as f:
    f.write("Hello")