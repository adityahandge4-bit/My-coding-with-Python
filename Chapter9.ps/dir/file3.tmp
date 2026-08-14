import os

# Get the current working directory
current_directory = os.getcwd()

# Loop through all files in the current directory
for file in os.listdir(current_directory):
    if file.endswith(".tmp"):
        os.remove(file)
        print(f"{file} deleted successfully.")

print("All temporary files have been removed.")