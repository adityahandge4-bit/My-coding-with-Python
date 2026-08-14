# Write a program to find out whether a file is identical and matches the content of another file.

with open("this.txt1","r") as f:
    content=f.read()
with open("file.txt","r") as f:
    content1=f.read()

if(content==content1):
    print("yes both files are idntical")
else:
    print("no the files are not identical")


