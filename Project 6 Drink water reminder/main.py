import time
from plyer import notification
while True:
    print("Please sip some water!")
    notification.notify(title="Please drink some water",
                        message="You need to drink some water")
    time.sleep(60*60)
    

# To be noted if you want to terminate the program just do this step:
#Open task manager(ctrl+shift+Esc)
# look for :
# python.exe or thre will be the vs code mentiined just click it and say end the program so that thi rogram will end.