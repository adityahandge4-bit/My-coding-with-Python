# To write a python programme for making 
# dictionary of Hindi words with values in English language

# Dict_={"Gadha":"Donkey",
# "Billi":"Cat",
# "Asur":"Demon",
# "Pappa":"Father"}

# d=(input("Enter the name of word you want meaning of: "))
# print(Dict_[d]) # Use of dictionary is there hence to be considered on higher preference is that terms inside the dictionary should alwways be written inside the square bracket

# or method

Dict_={"Gadha":"Donkey",
"Billi":"Cat",
"Asur":"Demon",
"Pappa":"Father"}
word=input("Enter the name of Hindi word:  ")
print("English meaning: ",Dict_.get(word, "Word not found"))















# Dict_={"Kela":"Banana",
#        "Billi":"Cat",
#        "Ghoda":"Horse",
#        "Insaan":"Human"}
# word=input("Enter the Hindi word:  ")
# print("English meaning is : ",Dict_.get(word,'word not found'))


