import math
a=math.sqrt(144)
print(a)

# A program for converting angles in degree to radians and find the vakue of the sin of angle of 90°
angle_degree=90
angle_radians=math.radians(angle_degree)
result=math.sin(angle_radians)
print(result)
# Otherwise use as follows
print(math.sin(math.radians(90)))  # First you have to convert the degrees into radians and then and only you will be able to get the value of sin 90 degree.


# Intall and import requests module and use it to fetch data fron "https://api.github.com"
import requests
a= requests.get("https://api.github.com")
print(a.text)