def goodday(name,ending="Take care"):
    print(f"Good day ,{name}")
    print(ending)
goodday('Aditya')
    # Remember that if you have given a default ending no need to
    #write it again in the ending
def goodday(name,ending="Take care"):
    print(f"Good day ,{name}")
    print(ending)
goodday('Aditya', 'Thanks')
#If you have given default even though give a ending to the 
#the code so python will consider the ending given later, not 
#the ending given in default