# Match case statement is primarily being used as a switch case statement in other programming languages. It is used to match the value of a variable against different cases and execute the corresponding block of code.
a=int(input("Enter the number:   "))
match a:
    case 1:
        print("You won the mercedes benz")
    case 45:
        print("You won an \"Apple laptop\"")
    case 90:
        print("You won the \"Rolex\" watch")
    case _:
        print("Better luck next time")

