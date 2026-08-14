import os

# Specify the directory path ('.' means the current working directory)
directory_path = 'problem 1.py_'#JUst say which directory you want to be listed here and then you can list it very easily.

try:
    # Get the list of all files and directories
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
        
except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory_path}'.")