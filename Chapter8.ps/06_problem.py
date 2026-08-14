# Write a python function which converts inches to cms.
# 1 inch=2.54 cm
def inch_to_cms(inch): # The thing or the numerical value that you want to convert would be written inside the closed bracket.
    return inch*2.54
inch=int(input("Enter the value in inches:  "))
c=inch_to_cms(inch)
print(f"{c}cm")
  