import shutil
shutil.rmtree("dir") # For completely deleting the directory
shutil.copy("File","File.txt") # Use for copying the certain file in another file 
shutil.move("File","Dir_") # used for moving the certain file inside the different directory 
shutil.copytree("Dir.txt","Dir 2") # Copy tree is used for making the new file from the existing file
# shutil.chown("Dir.txt","01_files.py")
shutil.copystat("04_files.append.py","06__line_by_line.py") # This is for linux operator
shutil.move("_os_module.py","Dir 1")
