import os
import datetime
from playsound import playsound
import time

os.system('clear')
alarmH = int(input("What hour do you want the alarm to ring? "))
alarmM = int(input("What minute do you want the alarm to ring? "))
amPm = str(input("am or pm? "))
stopH = 0
stopM = 1
os.system('clear')
print("Waiting for alarm",alarmH,alarmM,amPm)
if (amPm == "pm"):
        alarmH = alarmH + 12
while(1 == 1):

    if(alarmH == datetime.datetime.now().hour and alarmM == datetime.datetime.now().minute) :# When it gets to the desired time


        while(1 == 1):
            print("Time to wake up")
            playsound('nukesiren.mp3')
            time.sleep(1)
            if(alarmH + stopH == datetime.datetime.now().hour and alarmM + stopM == datetime.datetime.now().minute) :
                break

