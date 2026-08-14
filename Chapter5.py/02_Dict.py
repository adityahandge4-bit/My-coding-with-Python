d={} # This would be stated to be as a empty dictionary not empty set
print(type(d))
marks={
    "Harry":100,
    "Shubham":23,
    "Anirudh":56
}
print(marks.items())
print(marks.keys())
marks.update({"Harry":98, "Renuka":67})
print(marks)
print(marks.get("Harry"))
print(marks["Harry"])

print(marks.values())
marks.pop("Anirudh")
print(marks)

marks.clear()
print(marks)

# Difference between marks.get and marks[""] fuctions or methods
print(marks.get("Harry1")) # This method will show None variable version
print(marks["Harry1"])       # This method will show error
