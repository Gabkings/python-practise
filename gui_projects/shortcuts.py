from tkinter import *
from tkinter import ttk 

window = Tk()
window.geometry('400x400')
def shortcut(action):
    print(action)

window.bind('<Control-c>',lambda e:shortcut('copy'))
window.mainloop()