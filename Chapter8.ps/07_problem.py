# Write a python function to remove a given word from a list and strip it at the same time
def rem(l,word):
   l=["Aditya","Harry","Saikishore","Ramchandran","Janaki"]
   l.remove(word)
   return l
print(rem('l',"Saikishore"))

# Above method is regarding just to remove any word
# But we now have to strip the word placed in list so follow 
# the following method

def remove(list,word):
   n=[]
   for item in list:
      if not (item==word):
        n.append(item.strip(word))
   return n

list=["Harry","Aditya", "Ramchandran","rry"]

print(remove(list,'rry'))
         