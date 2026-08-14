numbers=[1,2,3,4,56,6,99,100]
def square(x):
    return x**2
print(list(map(square,numbers)))
# Here I just run the square function inside the numbers list so that the square of the listed elements inside the numbers(list) will be printed.Whereas map is used for that purpose only which will direct the square function inside the numbers (list)
print(list(map(lambda x:x**2,numbers)))