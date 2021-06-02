import datetime
import tkinter as Tkinter

import math
import time
from tkinter import *
import tkinter

from pygame import mixer
#import alarm

class main(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.x = 70
        self.y = 70
        self.window_management()
        self.length = 50
        self.create_canvas_for_shapes()
        self.creating_background()
        self.creating_stick()

    def window_management(self):
        self.geometry('140x140')
        self.resizable(0,0)
        self.title("Alarm Clock")
        #self.overrideredirect(1)

        self.right_click = tkinter.Menu(self, tearoff=0)
        self.right_click.add_command(label="Set Alarm", command= winAlarm)
        self.right_click.add_command(label="Quit", command=self.destroy)
        self.bind("<Button-3>", self.right_click_menu)


    def creating_background(self):
        self.image = Tkinter.PhotoImage(file='clock.gif')
        self.canvas.create_image(70,70, image=self.image)
        return

    def create_canvas_for_shapes(self):
        self.canvas = Tkinter.Canvas(self, bg='black')
        self.canvas.pack(expand='no', fill='both')
        return

    def creating_stick(self):
        self.stick = []
        for i in range(3):
            store=self.canvas.create_line(self.x, self.y,self.x+self.length,self.y+self.length,width=2, fill='black')
            self.stick.append(store)
        return
    
    def right_click_menu(self, event):
        try:
            self.right_click.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.right_click.grab_release()

    def update_class(self):
        now = time.localtime()
        t = time.strptime(str(now.tm_hour), "%H")
        hour = int(time.strftime( "%I", t)) * 5
        now = (hour, now.tm_min, now.tm_sec)
        for n,i in enumerate(now):
            x,y = self.canvas.coords(self.stick[n])[0:2]
            cr = [x,y]
            cr.append(self.length*math.cos(math.radians(i*6) - math.radians(90)) + self.x)
            cr.append(self.length*math.sin(math.radians(i*6) - math.radians(90)) + self.y)
            self.canvas.coords(self.stick[n], tuple(cr))
        return


def winAlarm():
    global winAlarm, inHrs, inMin, inSec
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
    Button(winAlarm, text="Set Alarm", command=setalarm, bg="DodgerBlue2", fg="white", font = ('arial', 20, 'bold')).grid(row=4, columnspan=3)
    timeleft = Label(winAlarm, font = ('arial', 20, 'bold'))
    timeleft.grid()


def setalarm():
    alarmtime=f"{inHrs.get()}:{inMin.get()}:{inSec.get()}"
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




if __name__ == '__main__':
    root = main()

    while True:
        root.update()
        root.update_idletasks()
        root.update_class()