friends = {}

for i in range(4):
    name = input(f"Enter name of friend {i+1}: ")
    language = input(f"Enter favorite language of {name}: ")
    
    friends[name] = language

print("Dictionary of friends and their favorite languages:")
print(friends)