# while(data:=(input("Enter the syntex that you wish: "))):
#     if data=="quit":
        
#         break
#     else:
#         print(data)

# making use of walrus operator for list comprehension
list=["python","rocks","ai"]
new_list=[n for w in list if(n:=len(w))>4] # here length of the words inside the list is being assigned to the n
print(new_list)



    