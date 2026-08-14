import os
def arrange_files(files,ext):
    file_withextension=[file for file in files if file.endswith(ext)]
    print(file_withextension)

    # i=1
    # for file in file_withextension:
    #     os.rename(file,f"photo-{i}{ext}")
    #     i+=1
    os.mkdir("My_photos")
    for i,file in enumerate(file_withextension):
        os.rename(file,f"My_photos/Photo-{i+1}{ext}") # This will add all the image file inside a seperate folder for greater accessibility
if __name__=="__main__":
    files=os.listdir()
    arrange_files(files,".jpg")