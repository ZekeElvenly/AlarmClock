from time import *
from tkinter import *
import time
import datetime
import tkinter
from pygame import mixer



def winAlarm():
    winAlarm = tkinter.Tk()
    winAlarm.title('Set Alarm')
    winAlarm.wm_resizable(0,0)
    hrs = StringVar()
    mins = StringVar()
    secs = StringVar()
    Label(winAlarm, font = ('arial', 14, 'bold'), text="Take a Short Nap!").grid(row=1, column=2)
    inHrs = Spinbox(winAlarm, textvariable=hrs,from_=0,to=23, width=5, font = ('arial', 14, 'bold'))
    inHrs.grid(row=2, column=1)
    inMin = Spinbox(winAlarm, textvariable=mins, from_=0, to=59, width=5, font = ('arial', 14, 'bold'))
    inMin.grid(row=2, column=2)
    inSec = Spinbox(winAlarm, textvariable=secs, from_=0, to=59, width=5, font = ('arial', 14, 'bold'))
    inSec.grid(row=2, column=3)
    Button(winAlarm, text="Set Alarm", command=lambda : setalarm(inHrs, inMin ,inSec), bg="DodgerBlue2", fg="white", font = ('arial', 14, 'bold')).grid(row=3, column=2)
    #timeleft = Label(frame, font = ('arial', 14, 'bold'))
    #timeleft.grid(row=4, column=3)


def setalarm(hrs, mins, secs):
    alarmtime=str(f"{hrs.get()}:{mins.get()}:{secs.get()}")
    settime = time.strptime(alarmtime, "%H:%M:%S")
    parsetime = time.strftime("%H:%M:%S", settime)
    #print(alarmtime)
    print(parsetime)
    if(parsetime!="::"):
        alarmclock(parsetime)

def alarmclock(alarmtime):
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
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


