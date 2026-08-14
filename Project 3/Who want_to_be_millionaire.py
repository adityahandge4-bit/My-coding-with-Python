questions=[
    [ "Which planet in our solar system is known for having the most prominent and extensive ring?","Jupiter","saturn","Neptune","Uranus",2],
    ["What is the capital city of Australia?",  "Sydney",  "Melbourne",      "Canberra",  "Brisbane",3],

    ["Which element on the periodic table has the chemical symbol 'O'?",  "Oxygen",  "Gold", "Hydrogen","Platinum", 1],

    ["Who painted the famous 16th-century portrait known as the Mona Lisa?",      "Michelangelo",  "Vincent van Gogh",  "Leonardo da Vinci",  "Pablo", 3],

   [" What is the longest river in the world?",  "Amazon River",  "Nile River",      "Yangtze River",  "Mississippi River",2],

    ["Which gas do plants primarily absorb from the atmosphere to perform     photosynthesis?", " Carbon Dioxide",  "Oxygen",  "Nitrogen",  "Hydrogen",1],

    ["How many bones are found in a standard adult human body?",  "106",      "206", "567", "406",  2],

    ["Which country is the largest by land area?",  "Canada",  "China",  "United States",  "Russia",  4],

    ["Who is known as the Father of the Indian Navy?..","Shivaji Maharaj","Columbus","Porus","Alexander Sikandar",1],
]

prizes=[1000,1500,2000,2500,3000,5000,10000,20000,500000]
i=0  # This is written outside the loop because the terms would be get added that are in the list
for question in questions:# For every question should be printed for that purpose using a loop is a smarter way to print all the questons in a sequential order.
    print(question[0])
    print(f"a.{question[1]}")# Why we use the list method so the reason is that the things to be printed sequentially and for ordered management.
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")
    a=int(input("Enter your answer.1 for a,2 for b,3 for c,4 for d: "))
    if(question[5]==a):
        print("Correct Answer")
    else:
        print(f"Incorrect,The correct answer is {question[5]}")
        print("Better luck next time")
        break
    print(f"You got {prizes[i]}")
    i+=1   # here the terms inside the list made with name prizes would be addded inside the loop accordingly by looping over again and again.

  