#Python Ver:    3.7.5
#
#Author:        Robert Ryan
#               10-17-2019
#Purpose:       GUI with Tkinter - creating GUI from Step 121
#
#Tested OS:     Windows 10

#Importing modules needed for this project
from tkinter import *
import tkinter as tk
import tkinter.constants, tkinter.filedialog

class ParentWindow(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self,master, *args, **kwargs)

        self.master=master
        self.master.minsize(480,70)
        self.master.maxsize(480,70)
        self.master.title('Directory Path')

        #form text boxes
        self.txtBrowse1 = tk.Entry(self.master,text='')
        self.txtBrowse1.grid(row=1,column=1,columnspan=3,padx=(30,0),pady=(25,0),ipadx=(99),ipady=(2),sticky=N+E)

        #buttons for the form
        self.btnBrowse1 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda:askDir(self))
        self.btnBrowse1.grid(row=1,column=0,padx=(15,0),pady=(25,0),sticky=N+E)


def askDir(self):
    dirPath = tkinter.filedialog.askdirectory()
    if dirPath:
        self.txtBrowse1.delete(0,END)
        self.txtBrowse1.insert(0,dirPath)


if __name__=='__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
