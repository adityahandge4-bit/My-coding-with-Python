import sys
def search_word(word,string): # It meant search that required word inside the string that i have provided
    return string.count(word)

if __name__=="__main__":
    filename=sys.argv[1]
    word=sys.argv[2]
    with open(filename) as f:
        string=f.read()
        n=search_word(word,string)
        print(f"There are {n} occurences of the {word} in the {filename}")