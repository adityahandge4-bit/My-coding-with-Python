with open("log.txt1","r") as f:
    content=f.read()

    if("python" in content):
        print("Yes, python is present in the file")
    else:
        print("No, python is not present in the file")