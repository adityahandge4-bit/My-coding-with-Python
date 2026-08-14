# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13-year-old.
def generateTables(n):
    table= ""
    for i in range(1,11):
        table+= f"{n} x {i}= {n*i}\n"
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2,21):
    generateTables(i)

# This way of code is written so that the everytime new file will be opened and the text form of the file will be form by writing tables/table_{n}.txt
# so that everytime the table from 2 till 21 table will be printed respectively in each and every text file serially














# def generatetables(n):
    #   tables=""
    # for i in range(1,11):
        # table+= f"{n}x{i}={n*i}\n"
    # with open(tables/table_{n}.txt,"w")
    # f.write(table)
# for i in range (2,21):
    # generatetables(i)