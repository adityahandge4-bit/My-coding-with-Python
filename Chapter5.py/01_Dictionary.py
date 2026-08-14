marks={
    "Harry":100,
    "Shubham":23,
    "Anirudh":56
}
print(marks)
print(marks["Harry"]) # This is for accessibility
# Dictionary is actually a type of key value pattern 
# We always write the keys inside the quote that is the keys are hashable so that the python can hash the keys internally
"""1. Tuples
2. sets
3. Strings 
4. Dictionaries 
are hashable 
but lists are not hashable"""

# For accesibilty and for modifying the certain terms inside the dictionary
print(marks["Shubham"])
marks["Shubham"]=99
print(marks)

# With this way we can access certain term inside the dictionry
