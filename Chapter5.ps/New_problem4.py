# Create a dictionary of three friends and their phone numbers
# friends={}
# a=input("Enter you name:  ")
# b=input("Enter you phone number:  ")
# friends.update({a:b})
# a=input("Enter you name:  ")
# b=input("Enter you phone number:  ")
# friends.update({a:b})
# a=input("Enter you name:  ")
# b=input("Enter you phone number:  ")
# friends.update({a:b})


# print(friends)
def friends_info():
    n=int(input("Enter the number: "))
    friends={}
    for i in range(n):
        a=input(f"Enter you name{i+1}:  ")
        b=input(f"Enter you phone number{i+1}:  ")
        friends.update({a:b})
    print(friends)
friends_info()


