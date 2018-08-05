from tkinter import *
from tkinter import ttk 

def resz(ev=None):
    #global alabel
    return alabel.configure(font = 'Aria -%d bold' % scale.get())
window = Tk()
window.geometry('500x500')

alabel = ttk.Label(text='Gabriel Gitonga', font='Aria -12 bold')
alabel.pack(fill='y',expand=1)
scale = ttk.Scale(window,from_=0, to = 40,command = resz)
scale.set(20)
scale.pack(fill='x',expand=1)

window.mainloop()