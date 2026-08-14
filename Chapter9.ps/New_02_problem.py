with open("file tasks.txt","w") as f:
    f.write("Python which is my favourite language and\n I learn it with very aspiration and\n I like to learn it a lot.")

with open("file tasks.txt","a") as f:
    f.write("Task completed!")

with open("file tasks.txt","r") as f:
    for line in f.readlines():
         print(line) # By making use of f.readlines() we can enlist all the lines inside the file.tasks.txt inside the list
