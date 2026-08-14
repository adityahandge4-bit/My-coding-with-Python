# Create the tuple for printing the elements inside the tuples
coordinates=(10,20)
print(coordinates[0:])
# Making use of the tuples for modifying the tuple
# coordinates[0]=50
# print(coordinates)  # To be noted this will throw the error

# Convert the tuple to the list and change the first element to 50, and convert it back to the tuple
lists=list(coordinates)
lists[0]=50
coordinates=tuple(lists)
print(coordinates)

# This is just a dilusion of changing the tuple but the original tuple has not changed we have made the new tuple

