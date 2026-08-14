# There are generally two types of modules in python as follows
"""1.Built in modules and
2. External modules"""
import pyttsx3     # This is an external module

engine=pyttsx3.init()
engine.say("My entire family is there with at DSMS Maha program")
engine.runAndWait()

import pyjokes  # External module
jokes= pyjokes.get_joke()
print(jokes)

import math # Built in module
print(math.sqrt(81))


import requests
r=requests.get("https://www.google.com")
print(r.text)
