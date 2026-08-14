# Write a python program using function to convert Celsius to Fahrenheit.
def c_to_f(c):
    return (9*c)/5 + 32
c=int(input("Enter the temperature in °C:  "))
d= c_to_f(c)
print(f"{round(d,2)}°F")

# Write a python programme to convert Fahrenheit to Celsius

def c_to_f(f):
    return 5*(f-32)/9
f=int(input("Enter the temperature in °F:  "))
e=c_to_f(f)
print(f"{round(e,2)}°C")




    