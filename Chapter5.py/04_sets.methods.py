# Methods of sets
# s={1,2,35,"monkey", 667,"Saurabh"}
# print(s,type(s))

# s.add(89)
# print(s, type(s))

# s.remove(667)
# print(s)




sets={23,34,55,67,89}
sets.add(12)
print(type(sets))
# sets.clear()
# sets.pop()
# sets.remove(12)
"""sets.remove(45)
If you write this code python extension will answer you as follows
sets.remove(45)
    ~~~~~~~~~~~^^^^
KeyError: 45"""
# Otherwise use the discard function which would remove only those elemnts that are actually present inside the set and will never throw the error
sets.discard(233455) # This will never throw the error
print(sets)
sets.remove(12)
print(sets)

