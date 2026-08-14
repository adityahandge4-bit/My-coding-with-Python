import os

# Rename the file
old_name = "myfile_.txt"          # Existing file name
new_name = "Adi.txt"

os.rename(old_name, new_name)

print("File renamed successfully.")