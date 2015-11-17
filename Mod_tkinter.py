__author__ = 'Sanchayan'
import sys
if sys.version_info > (3,0):
    from tkinter import *
else:
     from tkinter import *

import os.path

def calculate():
 global E1
 s = E1.get()
 size = os.path.getsize(s)
 global E2
 E2.insert(0,size)

def basic_verison():
    root = Tk()
    Label(root, text = 'Enter Path', fg = 'Brown').grid(row = 0, column = 0)
    E1 = Entry(root)
    E1.grid(row = 0, column = 1)

    Label(root, text = 'File Size', fg = 'Blue').grid(row = 2, column = 0)
    E2 = Entry(root)
    E2.grid(row = 2, column = 1)
    B = Button(root, text = 'Enter', fg = 'Blue', command = calculate)
    B.grid(row= 3, column = 1)
    root.mainloop()






class tkImpl(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        #Tk.iconbitmap(self,default='C:\Users\Sanchayan\Documents\GitHub\HackerRanksTypesolutions\AutoRun.ico')
        Tk.title(self,'My desktop app')
        # the container ill have all the componenets of tkinter App
        container = Frame(self)## frame is the Empty window
        ## The two wyas we can put the entitie sin tkinter is by using a pack or an grid
        ## The pack is a quick pack in a bag kind of thing where the organing options rae less
        container.pack(side='top',fill='both',expand=True)
        # fill is filling the window frame , Expand is maximise option
        container.rowconfigure(0,weight=1)
        container.columnconfigure(0,weight=1)# is row starting point and weight is priority

        #This frames are windows whicjh may be multiple for an app on a button click a new frame emerges
        self.frames = {}
        for F in (Startpage, PageOne):
            frame = F(container, self
            self.frames[F] = frame
            print("frame",frame)
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Startpage)
        frame = Startpage(container,self)
        #add the frame in Frames
        self.frames[Startpage]=frame
        #A grifd is declsared which s row sand column 2d arrsy
        frame.grid(row=0,column=0,sticky='nsew')
        self.show_frame(Startpage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
def qf(quickPrint):
    print(quickPrint)

class Startpage(Frame):
     def __init__(self,parent,controller):
         Frame.__init__(self,parent)
         label = Label(self,text='Start page')
         label.pack(pady=10,padx=10)
         button = Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
         button.pack()
         #button2 = Button(self, text="Visit Page 2",command=lambda: controller.show_frame(PageTwo))
         #button2.pack()

class PageOne(Frame):
     def __init__(self,parent,controller):
         Frame.__init__(self,parent)
         #label = Label(self,text='Page One',fg = 'Brown')
         #label.pack(pady=10,padx=10)
         #At this point we crated two Labels (2d Arrays ) which we can  refer by rowid later
         Label(self,text='First name').grid(row=0)
         Label(self, text="Last Name").grid(row=1)

         e1 = Entry(self)
         e2 = Entry(self)
         e1.insert(10,'Firstname')
         e2.insert(10,'Lastname')

         e1.grid(row=0, column=1)
         e2.grid(row=1, column=1)
         # Entry of Radio Buttons
         v = IntVar()

         Label(self, text="""Choose a  language:""",justify = LEFT,padx = 20).grid(row=2)
         Radiobutton(self,
                     text="Bengali",
                     padx = 20,
                     variable=v,
                     command=ShowChoice(v),
                     value=1).grid(row=2)
         Radiobutton(self,
                     text="assamese",
                     padx = 20,
                     variable=v,
                     command=ShowChoice(v),
                     value=2).grid(row=3)

         button = Button(self, text="Back", command=lambda: controller.show_frame(Startpage))

        # button.pack()
         #button2 = Button(self, text="Visit Page 2",command=lambda: controller.show_frame(PageTwo))
         #button2.pack()

def ShowChoice(v):
    print(v.get)

if __name__=="__main__":
    #basic_verison()
    app = tkImpl()
    app.mainloop()