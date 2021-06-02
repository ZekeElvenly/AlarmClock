import tkinter as tk

class guiapp(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.value = 0.0
        self.alive = True
        self.list_for_toplevel = []
        btn = tk.Button(self.master, text = "Click", command = self.TextWindow)
        btn.pack()

    def TextWindow(self):
        self.textWindow = tk.Toplevel(self.master)
        self.textFrame = tk.Frame(self.textWindow)
        self.textFrame.pack()
        self.textArea = tk.Text(self.textWindow, height = 10, width = 30)
        self.textArea.pack(side = "left", fill = "y")

        bar = tk.Scrollbar(self.textWindow)
        bar.pack(side = "right", fill = "y")
        bar.config(command = self.textArea.yview)
        self.alive = True
        self.timed_loop()

    def timed_loop(self):
        if self.alive == True and tk.Toplevel.winfo_exists(self.textWindow):
            self.master.after(1000, self.timed_loop)
            self.value += 1
            self.list_for_toplevel.append(self.value)
            self.textArea.delete(1.0, "end-1c")
            for item in self.list_for_toplevel:
                self.textArea.insert('end', "{}\n".format(item))
                self.textArea.see('end')
        else:
            self.alive = False

if __name__ == "__main__":

    root = tk.Tk()
    root.geometry("800x480")
    myapp = guiapp(root)
    root.mainloop()