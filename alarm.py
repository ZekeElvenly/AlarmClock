from time import *
from tkinter import messagebox
from tkinter import *
import multiprocessing
import time
import datetime
import tkinter as tk
from playsound import playsound

class mainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Alarm Clock')
        self.iconphoto(False, PhotoImage(file='icon.png'))
        self.wm_resizable(0,0)
        self.winAlarm()

    def winAlarm(self):
        self.bind('<Return>', lambda e: self.setalarm(self.inHrs, self.inMin, self.inSec))
        hrs = StringVar()
        mins = StringVar()
        secs = StringVar()
        self.setTime = Label(self, font = ('arial', 14, 'bold'), text="Take a Short Nap!")
        self.setTime.grid(row=1, column=2)
        self.inHrs = Spinbox(self, textvariable=hrs,from_=0,to=23, width=3, font = ('arial', 14, 'bold'))
        self.inHrs.grid(row=2, column=1)
        self.inMin = Spinbox(self, textvariable=mins, from_=0, to=59, width=3, font = ('arial', 14, 'bold'))
        self.inMin.grid(row=2, column=2)
        self.inSec = Spinbox(self, textvariable=secs, from_=0, to=59, width=3, font = ('arial', 14, 'bold'))
        self.inSec.grid(row=2, column=3)
        self.startBtn = Button(self, text="Set Alarm", command=lambda : self.setalarm(self.inHrs, self.inMin ,self.inSec), bg="DodgerBlue2", fg="white", font = ('arial', 12))
        self.startBtn.grid(row=4, column=2)
        Button(self, text="Stop", command=lambda : self.stopAlarm(), bg="DodgerBlue2", fg="white", font = ('arial', 12)).grid(row=4, column=1)
        Button(self, text="Quit", command=lambda : quitApp(), bg="DodgerBlue2", fg="white", font = ('arial', 12)).grid(row=4, column=3)
        #self.setTime = Label(self, text='Set your wake up time!', font = ('arial', 11))
        #self.setTime.grid(row=3, column=2)

        def quitApp():
            try:
                if self.alarmRun.is_alive():
                    self.stopAlarm()
                    self.destroy()
                else:
                    self.destroy()
            except AttributeError:
                self.destroy()

    def stopAlarm(self):
        try:
            self.bind('<Return>', lambda e: self.setalarm(self.inHrs, self.inMin, self.inSec))
            self.startBtn["state"] = "normal"
            self.startBtn["bg"] = "DodgerBlue2"
            self.setTime["text"] = "Take a Short Nap!"
            self.alarmRun.terminate()
            self.playAlarm(alarmsound=False)
            messagebox.showinfo('Alarm','Alarm has been stopped!')
            print("Alarm has been stopped")
        except AttributeError:
            messagebox.showwarning('Alarm',"Alarm hasn't set yet!")

    def disable_shortcut(self):
        pass

    def setalarm(self, hrs, mins, secs):
        self.bind('<Return>', lambda e: self.disable_shortcut())
        self.startBtn["state"] = "disable"
        self.startBtn["bg"] = "grey"
        alarmtime=str(f"{hrs.get()}:{mins.get()}:{secs.get()}")
        settime = time.strptime(alarmtime, "%H:%M:%S")
        self.parsetime = time.strftime("%H:%M:%S", settime)
        #print(alarmtime)
        self.alarmRun = multiprocessing.Process(target=lambda : self.alarmclock(self.parsetime, run=True))
        print(self.parsetime)
        if(self.parsetime!="::"):
            self.alarmRun.start()
            self.setTime["text"] = "Set to {}".format(self.parsetime)
            messagebox.showinfo('Alarm','Alarm has been set to {}'.format(self.parsetime))

    def alarmclock(self, alarmtime, run):
        while run == True:
            time.sleep(1)
            time_now=datetime.datetime.now().strftime("%H:%M:%S")
            print(time_now)
            if time_now==alarmtime:
                self.playAlarm(alarmsound=True)
                break

    def playAlarm(self, alarmsound):
        while alarmsound == True:
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
    

