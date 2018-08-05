from tkinter import *

window = Tk()

window.geometry('500x500-300+130')
def hello():
    a = b.get()
    mlabel = Label(text= a,font=10).pack()


# mlabutton1 = Button(text='Gabriel', relief = SUNKEN b).pack()
# mlabutton2 = Button(text='Gabriel', relief = FLAT).pack()
# mlabutton3 = Button(text='Gabriel', relief = RAISED).pack()
# mlabutton4 = Button(text='Gabriel', relief = RIDGE).pack()
# mlabutton5 = Button(text='Gabriel', relief = GROOVE).pack()

#mlabel = Label(text="Hello", fg='grey', bg='pink').grid(row = 1, column = 0, sticky = W)
mlabutton = Button(text='Gabriel', width = 150, height = 100,command = hello, font = 20, fg = 'red', bg='pink', activebackground = 'white', activeforeground ='black',cursor = 'plus',bitmap ='questhead',relief = RIDGE ).pack()
b = StringVar()
text = Entry(textvariable = b).pack()
window.title('hello world')

window.mainloop()