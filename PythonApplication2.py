from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os


def newFile():
    global file
    root.title("united_notepad")
    file=None
    TextArea.delete(1.0,END)
    

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",
                         filetypes=[("All Files","*.*"),
                                    ("Text Files","*.txt*")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(defaultextension=".txt",
                         filetypes=[("All Files","*.*"),
                                    ("Text Files","*.txt*")])

        if file=="":
            file=None
        else:
            f=open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+"-Notepad")
            print("file saved")

    else:
        f=open(file,'w')
        f.write(TextArea.get(1.0,END))
        f.close()




        
                

def Exit():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def help():
    showinfo("Notepad","Notepad by Aditya Sahore")

if __name__=='__main__':
    root=Tk()
    root.title("untitled-Notepad")
    #root.wm_iconbitmap("1.ico")
    root.geometry("644x788")

    #Add textArea
    TextArea=Text(root,font='arial 16')
    file=None
    TextArea.pack(expand=True,fill=BOTH)

    #add a menu
    MenuBar=Menu(root,)

    #add file menu
    Filemenu=Menu(MenuBar,tearoff=0)
    #create a new file
    Filemenu.add_command(label='New',command=newFile)

    #open an existing file
    Filemenu.add_command(label='open',command=openFile)

    #save a file
    Filemenu.add_command(label='save',command=saveFile)
  
    Filemenu.add_command(label='exit',command=Exit)

    MenuBar.add_cascade(label='File',menu=Filemenu)

    #Edit menu starts
    Editmenu=Menu(MenuBar,tearoff=0)

    Editmenu.add_command(label='cut',command=cut)

    Editmenu.add_command(label='copy',command=copy)

    Editmenu.add_command(label='paste',command=paste)

    MenuBar.add_cascade(label='Edit',menu=Editmenu)
    

    #help menu starts

    Helpmenu=Menu(MenuBar,tearoff=0)

    Helpmenu.add_command(label='about us',command=help)

    MenuBar.add_cascade(label='Help',menu=Helpmenu)

    root.config(menu=MenuBar)

    scroll=Scrollbar(TextArea)

    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)
    

    

    root.mainloop()


    



