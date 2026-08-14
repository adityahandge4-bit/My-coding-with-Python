# for empty set it is written as follow
# e= set()   # This is consider to be as a empty set
# print(type(e))
#But if you do as follows you will get empty dict. not set

# a={}    # This would be empty dictionary
# print(type(a))



s={23,43,22,12,89,90}
print(s,type(s))

# Sets are unorderd unique collection so that the elements in the ets are not scriptable
# As follows
print(s[1])
"""File "d:\ADITYA PYTHON\Chapter5.py\03_sets.py", line 16, in <module>
    print(s[1])
          ~^^^
TypeError: 'set' object is not subscriptable"""
# The above statement would be printed so you should know when to use this method for listing the terms 
# To be noted that whenever you have to list the things so this method is allowed only in the things as mentioned
#     1. In lists
#     2. In tuples
#     3. In strings
# You cannot use this method innside the sets since they are unordered
