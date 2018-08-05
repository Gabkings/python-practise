from tkinter import *
class Application(Frame):
    #frame is used to group and organize other widgets
    #It is basically a container onject for all widget an app is gooing to use
    #This is a special function that is called when a instance of a class is created
    def _init_(self,master):
        #self is the refernce to current instance of the class and master rep the parent widget
        #the super is special builtin function which return a proxy object to delegate method calls
        #it is used to initialize the frame 
        super(Application,self)._init_(master)
        self.task=""
        self.UserIn = StringVar()
        #grid() method is used to register widgets with the grid geometry manager
        #The geometry manager manages the placement and layouts of the elements of the GUI
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        #entry widget is used to accept single line taxt string from user
        #insertwidth is the width of insertion cursor
        self.use_input= Entry(self, bg= "blue", bd = 29,insertwidth = 4,width = 24, font = ("Verdana", 20, "bold"), textvariable= self.UserIn, justify = RIGHT)
        self.user_input.grid(columnspan = 4)

        self.user_input.insert(0, "0")

        self.button1 = Button(self, bg="red" , bd = 12,text ="7", padx = 33, pady = 25,font = ("Helvetica", 20, "bold"), command = lambda : self.buttonClick(7))
        self.button1.grid(row = 2, column = 0, sticky = w)
        
        self.button2 = Button(self, bg="red" , bd = 12,text ="8", padx = 35, pady = 25,font = ("Helvetica", 20, "bold"), command = lambda : self.buttonClick(8))
        self.button2.grid(row = 2, column = 1, sticky = w)

        self.button3 = Button(self, bg="red" , bd = 12, text ="9", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"), command = lambda : self.buttonClick(9))
        self.button3.grid(row = 2, column = 2, sticky = w)

        self.button4 = Button(self, bg="red" , bd = 12, text ="4", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"), command = lambda : self.buttonClick(4))
        self.button4.grid(row = 3, column = 0, sticky = w)

        self.button5 = Button(self, bg="red" , bd = 12,text ="5", padx = 35, pady = 25,font = ("Helvetica", 20, "bold"), command = lambda : self.buttonClick(5))
        self.button5.grid(row = 3, column = 1, sticky = w)

        self.button6 = Button(self, bg="red" , bd = 12,text ="6", padx = 33, pady = 25,font = ("Helvetica", 20, "bold"),command = lambda : self.buttonClick(6))
        self.button6.grid(row = 3, column = 2, sticky = w)

        self.button7 = Button(self, bg="red" , bd = 12, text ="1", padx = 33, pady = 25,font = ("Helvetica", 20, "bold"),command = lambda : self.buttonClick(1))
        self.button7.grid(row = 4, column = 0, sticky = w)

        self.button8 = Button(self, bg="red" , bd = 12,text ="2", padx = 35, pady = 25,font = ("Helvetica", 20, "bold"),command = lambda : self.buttonClick(2))
        self.button8.grid(row = 4, column = 1, sticky = w)

        self.button9 = Button(self, bg="red" , bd = 12,
                              text ="3", padx = 33, pady = 25,
                              font = ("Helvetica", 20, "bold"),
                              command = lambda : self.buttonClick(3))
        self.button9.grid(row = 4, column = 2, sticky = w)

        self.button10 = Button(self, bg="red" , bd = 12,
                              text ="0", padx = 33, pady = 25,
                              font = ("Helvetica", 20, "bold"),
                              command = lambda : self.buttonClick(0))
        self.button10.grid(row = 5, column = 0, sticky = w)

        self.Addbutton = Button(self, bg="red" , bd = 12,
                              text ="+", padx = 36, pady = 25,
                              font = ("Helvetica", 20, "bold"),
                              command = lambda : self.buttonClick("+"))
        self.Addbutton.grid(row = 2, column = 3, sticky = w)

        self.Subbutton = Button(self, bg="red" , bd = 12,
                              text ="-", padx = 39, pady = 25,
                              font = ("Helvetica", 20, "bold"),
                              command = lambda : self.buttonClick("-"))
        self.Subbutton.grid(row = 3, column = 3, sticky = w)

        self.Multbutton = Button(self, bg="red" , bd = 12,
                              text ="*", padx = 38, pady = 25,
                              font = ("Helvetica", 20, "bold"),
                              command = lambda : self.buttonClick("*"))
        self.Multbutton.grid(row = 4, column = 3, sticky = w)

        self.Divbutton = Button(self, bg="red" , bd = 12,
                              text ="/", padx = 39, pady = 25,
                              font = ("Helvetica", 20, "bold"),
                              command = lambda : self.buttonClick("/"))
        self.Divbutton.grid(row = 5, column = 3, sticky = w)


        self.Equalbutton = Button(self, bg="red" , bd = 12,
                              text ="=", padx = 100, pady = 25,
                              font = ("Helvetica", 20, "bold"))
        self.button1.grid(row = 5, column = 1, sticky = w,columnspan = 2)


        self.Clearbutton = Button(self, bg="red" , bd = 12,
                              text ="AC", width = 28,padx = 7,
                              font = ("Helvetica", 20, "bold"),
                              command = self.ClearDisplay)
        self.button1.grid(row = 1, columnspan = 4, sticky = w)

    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer
        except SyntaxError as e:
            self.displayText("Invalid Syntax")
            self.task = ""
        
    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")
calculator = Tk()

calculator.title("Calculator")
app = Application(calculator)
calculator.resizable(width = False, height = False)
calculator.mainloop()
