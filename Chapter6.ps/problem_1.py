# Write a program to find the greatest of four numbers entered by the user.
def greatest_function():
    n=[]
    for i in range(1,5):
        n.append(int(input(f"Enter the number {i} :")))
        
    if n[0]>n[1] and n[0]>n[2] and n[0]>n[3]:
        print(f"{n[0]} is greatest of all")
    elif n[1]>n[0] and n[1]>n[2] and n[1]>n[3] :
        print(f"{n[1]} is greatest of all")
    elif n[2]>n[1] and n[2]>n[3] and n[2]>n[0] :
        print(f"{n[2]} is greatest of all")
    elif n[3]>n[1] and n[3]>n[2] and n[3]>n[0] :
        print(f"{n[3]} is greatest of all")
greatest_function()

def greatest_function():
    n=[]
    for i in range(1,5):
        n.append(int(input(f"Enter the number {i} : ")))
    greatest=max(n)
    print(f"{greatest} is greatest of all")
greatest_function()



    

    
     
    
    
