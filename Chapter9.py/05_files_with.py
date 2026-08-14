# Use of file method
f=open("file.txt.2")
data=f.read()
print(data)
f.close()
# But by making use of with in files to simplify
with open("file.txt.2") as f:# with is context manager
    print(f.read())

# With this method you don't have to add f.close() at ending