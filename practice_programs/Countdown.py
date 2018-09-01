from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime


global endTime

def quit(*args):
    root.destroy()

def cant_wait():
    timeLeft = endTime - datetime.datetime.now()
    #trim the microsecind part of the time
    timeLeft = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)
    #display the time left
    txt.set(timeLeft)
    #initiate the countdown after 1 second
    root.after(1000,cant_wait)

root = Tk()
root.attributes('-fullscreen',False)
root.bind("x",quit)
root.after(1000,cant_wait)
#set the end date for count down
endTime = datetime.datetime(2018, 9, 29,0,0)
fnt = font.Font(family='Helvetica', size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt,foreground='white', background='black')
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
