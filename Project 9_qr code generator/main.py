"""
We are going to make the qr code by using the a python library and going to convert the url to qr code
"""
import qrcode
url=input("Enter the url: ")
file_name=input("Enter the name of the file: ")
if not(file_name.endswith(".png")):
    file_name=file_name +".png"
img=qrcode.make(url)
img.save(file_name)
# To download the image and image creator first step is to do "pip install pillow" module