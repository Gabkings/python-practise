from tkinter import *
from tkinter import ttk 

master = Tk()
def show_detail():
    return Label(text=e1.get()).grid(row = 3,column = 1)
def show_detail1():
    return Label(text=e2.get()).grid(row = 3,column = 2) 
def all():
    show_detail()
    show_detail1() 



Label(text='First Name:').grid(row = 0)
Label(text='Last Name:').grid(row = 1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row = 0,column = 1)
e2.grid(row = 1, column = 1)

#y = Label(text='show first')

#Label(text='show last').grid(row = 3,column = 2)
Button(master, text = 'Quit', command=master.quit).grid(row=4,column= 0)
Button(master, text = 'Show',command=all).grid(row=4,column= 1)



master.mainloop()