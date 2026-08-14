# Write a recursive function to calculate the sum of first n natural numbers.
# By my method

n=int(input("Enter the number:  "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

# Using recursive function


def sum(n):
  if(n==1): # We put the condition so that the recurrcive function can work smoothly and efficiently.
    return 1
  return sum(n-1)+n
print(sum(46))