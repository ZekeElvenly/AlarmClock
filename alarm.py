from time import strftime
from tkinter import *
import time
import datetime
import tkinter
from pygame import mixer



def winAlarm():
    winAlarm = tkinter.Tk()
    winAlarm.title('Set Alarm')  
    hrs = StringVar()
    mins = StringVar()
    secs = StringVar()
    Label(winAlarm, font = ('arial', 20, 'bold'), text="Take a Short Nap!").grid(row=1, columnspan=3)
    inHrs = Entry(winAlarm, textvariable=hrs, width=5, font = ('arial', 20, 'bold'))
    inHrs.grid(row=2, column=1)
    inMin = Entry(winAlarm, textvariable=mins, width=5, font = ('arial', 20, 'bold'))
    inMin.grid(row=2, column=2)
    inSec = Entry(winAlarm, textvariable=secs, width=5, font = ('arial', 20, 'bold'))
    inSec.grid(row=2, column=3)
    Button(winAlarm, text="Set Alarm", command=lambda : setalarm(inHrs, inMin ,inSec), bg="DodgerBlue2", fg="white", font = ('arial', 20, 'bold')).grid(row=4, columnspan=3)
    timeleft = Label(winAlarm, font = ('arial', 20, 'bold'))
    timeleft.grid()


def setalarm(hrs, mins, secs):
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime) 
    if(alarmtime!="::"):
        alarmclock(alarmtime)

def alarmclock(alarmtime):
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
            Label(winAlarm, font = ('arial', 20, 'bold'), text="Wake UP!", bg="DodgerBlue2", fg="white").grid(row=5, columnspan=3)
            print("Wake Up!")
            mixer.init()
            mixer.music.load(r'sound.wav')
            mixer.music.play()
            break




#    def alarmclock(alarmtime):
#        while True:
#            time.sleep(1)
#            time_now=datetime.datetime.now().strftime("%H:%M:%S")
#            if time_now==alarmtime:
 #               Wakeup=Label(, font = ('arial', 20, 'bold'), text="Wake UP!", bg="DodgerBlue2", fg="white").grid(row=5, columnspan=3)
#                print("Wake Up!")
#                mixer.init()
#                mixer.music.load(r'sound.wav')
#                mixer.music.play()
#                break


