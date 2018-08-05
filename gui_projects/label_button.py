from tkinter import Tk,Label,Button
from tkinter import *
from tkinter import ttk 

class My_GuI:
    """docstring for My_GuI"""
    def __init__(self, master):
        self.master = master
        self.label =Label(master,text='Greet')
        self.label.pack()

        self.button = Button(master,text='Greet',relief=SUNKEN,command=self.greet)
        self.button.pack()
        self.button = Button(master,text='Quit',relief=SUNKEN,command=master.quit)
        self.button.pack()

    def greet(self):
       return self.label.configure(text='Hello')


root = Tk()
My_GuI = My_GuI(root)
root.mainloop()
        
