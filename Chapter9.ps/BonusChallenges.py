# # Write a program that reads the file and creates another file with all words overted to uppercase
with open("problem_10.py","r") as f:
    content=f.read()

with open("new_file2","w") as f:
    f.write(content.upper())

# # Create a script that deletes all.tempfiles from the current directory using os and os.remove
# import os
# import os

# # Get the current working directory
# current_directory = os.getcwd()

# # Loop through all files in the current directory
# for file in os.listdir(current_directory):
#     if file.endswith(".tmp"):
#         os.remove(file)
#         print(f"{file} deleted successfully.")

# print("All temporary files have been removed.")

import os
import sys

def get_total_size(folder):
    total_size = 0

    # Loop through all items in the folder
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)

        # Check if the item is a file
        if os.path.isfile(item_path):
            total_size += os.path.getsize(item_path)

    return total_size


if __name__ == "__main__":
    folder = sys.argv[1]
    print(folder)
    if os.path.isdir(folder):
        size = get_total_size(folder)
        print(f"Total size of all files in '{folder}' is {size} bytes.")
    else:
        print("Error: The specified folder does not exist.")



