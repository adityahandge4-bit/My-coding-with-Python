while True:
    
    try:
       a=int(input("Enter the number 1: "))
       b=int(input("Enter the number 2: "))
       print("For the operation of addition print \"+\"\n, for the operation of subtraction print \"-\"\n, for multiplication use\"*\"\n, for division print \"/\"")
       if b=="quit":
        print("Good bye")
        break


      

       operation=input("Enter the operation: ")
       match operation:
           case "+":
               print(f"sum of two numbers is {a+b}")
           case "-":
               print(f"Subtraction of two numbers is {a-b}")
           case "*":
               print(f"Product of two numbers is {a*b}")
           case "/":
               print(f"Division of two numbers is {a/b}")
           case"_":
               print("")
    except ZeroDivisionError:
        if b==0:
            print("GOOD BYE!")
        break
        
        
        
   


    
    
