f=open("file.txt.2")
# lines=f.readlines()
# print(lines,type(lines))
# line1=f.readline() 
# print(line1,type(line1))
# line2=f.readline() 
# print(line2,type(line2))
# line3=f.readline() 
# print(line3,type(line3))
# f.close()

line=f.readline() # By opening the file the python interpretor read the lines inside the file and then print it according to the command.
while(line !=""):
    print(line)
    line=f.readline()
f.close()