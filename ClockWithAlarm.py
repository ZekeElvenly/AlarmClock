from time import *
from tkinter import ttk
from tkinter import *
import time
import datetime
import tkinter as tk
from playsound import playsound


class mainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Alarm Clock')
        self.wm_resizable(0,0)
        self.winAlarm()

    def winAlarm(self):
        hrs = StringVar()
        mins = StringVar()
        secs = StringVar()
        Label(self, font = ('arial', 14, 'bold'), text="Take a Short Nap!").grid(row=1, column=2)
        inHrs = Spinbox(self, textvariable=hrs,from_=0,to=23, width=3, font = ('arial', 14, 'bold'))
        inHrs.grid(row=2, column=1)
        inMin = Spinbox(self, textvariable=mins, from_=0, to=59, width=3, font = ('arial', 14, 'bold'))
        inMin.grid(row=2, column=2)
        inSec = Spinbox(self, textvariable=secs, from_=0, to=59, width=3, font = ('arial', 14, 'bold'))
        inSec.grid(row=2, column=3)
        Button(self, text="Set Alarm", command=lambda : self.setalarm(inHrs, inMin ,inSec), bg="DodgerBlue2", fg="white", font = ('arial', 14)).grid(row=3, column=2)
        #timeleft = Label(self, font = ('arial', 14, 'bold'))
        #timeleft.grid(row=4, column=3)

    def setalarm(self, hrs, mins, secs):
        alarmtime=str(f"{hrs.get()}:{mins.get()}:{secs.get()}")
        settime = time.strptime(alarmtime, "%H:%M:%S")
        parsetime = time.strftime("%H:%M:%S", settime)
        #print(alarmtime)
        print(parsetime)
        if(parsetime!="::"):
            self.alarmclock(parsetime)

    def alarmclock(self, alarmtime):
        while True:
            time.sleep(1)
            time_now=datetime.datetime.now().strftime("%H:%M:%S")
            print(time_now)
            if time_now==alarmtime:
                self.playAlarm()
                break

    def playAlarm(self):
        print("Wake Up!")
        playsound('Bangun, Bangsat.mp3')

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

if __name__ == '__main__':
    app = mainWindow()
    app.mainloop()

