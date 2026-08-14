import argparse

# Create a parser for command line arguments with a description
parser = argparse.ArgumentParser(description="Simple Calculator")

# Add required positional arguments for the two numbers
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")

# Add required positional argument for the operation to perform
parser.add_argument(
    "operation",
    choices=["add", "sub", "div", "mul"],
    help="Operation to perform: add, sub, div, or mul"
)

# Parse the command line arguments into the args object
args = parser.parse_args()
print(args)

# Perform the requested calculation and display the result
if args.operation == "add":
    print(f"The result is {args.num1 + args.num2}")
elif args.operation == "sub":
    print(f"The result is {args.num1 - args.num2}")
elif args.operation == "mul":
    print(f"The result is {args.num1 * args.num2}")
elif args.operation == "div":
    print(f"The result is {args.num1 / args.num2}")
else:
    # This branch should not be reached because argparse restricts operation values
    print("There's something error")

