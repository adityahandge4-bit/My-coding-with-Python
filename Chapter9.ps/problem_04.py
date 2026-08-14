# #A file contains a word “Donkey” multiple times. You need to write a program which
# replaces this word with ##### by updating the same file.

word="Donkey"

with open("file.txt 1","r") as f :
    content=f.read()

contentnew=content.replace(word,'#####')
with open("file.txt 1","w") as f :
    f.write(contentnew)
