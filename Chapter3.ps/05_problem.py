# Given sentennce use for replacing the certain word inside the the string
# String manipulation
sentence="Coding in Python is fun"
print(sentence.replace("fun","awesome"))
print(sentence.index("Python"))
print(sentence.upper())
# If two words in the sentence is common but you want to replace only one word inside it then you should do it as follows
sentence_="Coding in python is fun and fun"
print(sentence_.replace("fun","Amazing",1))
print(sentence_.replace("fun","amazing",2))
parts=sentence_.split("fun")
new_sentence=parts[0]+"fun"+parts[1]+"amazing"+parts[2]
print(new_sentence)
# If I want to change the second occurence then follow the method as follows
sentence = "apple is tasty and apple is healthy"

parts = sentence.split("apple")

new_sentence = parts[0] + "apple" + parts[1] + "mango" + parts[2]

print(new_sentence)

# If I want to change the all the occurences
# Just say as follows
print(sentence.replace("apple","mango"))












