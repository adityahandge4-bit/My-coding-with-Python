# Repeat program 4 for a list of such words to be censored.

words=["Donkey","Shweta","Hero","Notebook"]

with open("file.txt 1","r") as f :
    content=f.read()

for word in words: 
   content=content.replace(word,'#'*len(word))
with open("file.txt 1","w") as f :
    f.write(content)
