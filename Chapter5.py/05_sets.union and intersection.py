# Define two example sets of integers
s1 = {12, 23, 45, 67, 89, 0, 49, 99}
s2 = {22, 21, 47, 45, 89, 90}

# Print the union of s1 and s2 (all unique elements present in either set)
print(s1.union(s2))

# Print the intersection of s1 and s2 (elements common to both sets)
print(s1.intersection(s2))

# Check if the set {23, 45, 89} is a subset of s2 (all elements present in s2)
print({23, 45, 89}.issubset(s2))

# Check if s2 is a superset of s1 (contains all elements of s1)
print(s2.issuperset(s1))

# Check if the set {45, 89} is a subset of s2
print({45, 89}.issubset(s2))
