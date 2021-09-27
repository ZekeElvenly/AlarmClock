import tkinter as Tkinter
import multiprocessing
import math
import time
import datetime
from tkinter import *
import tkinter as tk
from playsound import playsound

class main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.x = 70
        self.y = 70
        self.window_management()
        self.length = 50
        self.create_canvas_for_shapes()
        self.creating_background()
        self.creating_stick()
        while True:
            self.update()
            self.update_class()
            self.update_idletasks()

    def window_management(self):
        self.geometry('140x140')
        self.resizable(0,0)
        self.title("Alarm Clock")
        #self.overrideredirect(1)

        self.right_click = tk.Menu(self, tearoff=0)
        self.right_click.add_command(label="Set Alarm", command=self.open_alarm)
        self.right_click.add_command(label="Quit", command=self.destroy)
        self.bind("<Button-3>", self.right_click_menu)

    def open_alarm(self):
        window = Window(self)
        window.grab_set()

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


class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

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
        #timeleft = Label(frame, font = ('arial', 14, 'bold'))
    #timeleft.grid(row=4, column=3)


    def setalarm(self, hrs, mins, secs):
        alarmtime=str(f"{hrs.get()}:{mins.get()}:{secs.get()}")
        settime = time.strptime(alarmtime, "%H:%M:%S")
        parsetime = time.strftime("%H:%M:%S", settime)
        alarmProcess = multiprocessing.Process(target=lambda : self.alarmclock(parsetime))
        #print(alarmtime)
        print(parsetime)
        if(parsetime!="::"):
            alarmProcess.start()

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

if __name__ == '__main__':
    main().mainloop()