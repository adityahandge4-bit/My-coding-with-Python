# Always remember that strings are immutable
name="Hello world"
print(len(name))
print(name.capitalize())
print(name.upper())
print(name.lower())
replaced=name.replace("world","Harry")# Print and changes all the occurences
print(replaced)
find_12=name.find('w') # Print only the first occurence of the given element
print(find_12)
print(name.count("o"))
print(name.title())
print(name.rstrip())
print(name.split(",")) # This functionality is being used to convert the given string into list
# But if you write as follows thn a list is reconverted into normal string form
# print(','.join(['Hello world']))
print(name.isalpha())
print(name.isdigit())
print(name.isalnum())