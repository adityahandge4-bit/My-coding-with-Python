# Basically os module is used for listing:
# 1. the directories
# It is being used for to get the current cwd
# Used for checking whether the directory exists or not
# Also for removing the empty directories
import os
a=os.listdir("dir")
print(a)
info=os.getcwd()
print(info)
print(os.path.exists("Adi_ifo.txt"))






