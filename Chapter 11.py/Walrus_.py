def very_slow_program():
    print("Something.....")
    print("Something.....")
    print("Something.....")
    print("Something.....")
    print("Something.....")
    print("Something.....")
    return 12
# a=very_slow_program()
if((a:=very_slow_program())>10): # If you missed the parenthesis=() ,to be given to the walrus operator it will considered it as a Booleans and print True
    print(a)
else:
    print("It's not greater than 10")


while(data:=input("Enter the value:  ")):  # By making use of walrus operator we can generally write and concatinate the code in a single line   
    print(data)
    if data=="q":
        break