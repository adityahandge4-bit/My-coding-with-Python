# Write a lambda function that adds two numbers and test it
sum=lambda x,y:(x+y)
print(sum(56,78))

# Create the list [1,2,3,4,5] and use map() with lambda function to get their squares
square= lambda x:x**2  # here first state the variable and then by using colon state what you have to do with the variable
list1=[1,2,3,4,5]
print(list(map(square,list1)))
# For printing the square of the numbers present in the list use the above method as listed above
# Here note a certain thing that in print funtion 
#in First time print list is used to list the square of the numbers inside the existing list and map is used to find the square of the numbers present in the given list and then square , list1 is used to make use of the terms or the numbers present in the list1 to be used for making the square of the numbers
