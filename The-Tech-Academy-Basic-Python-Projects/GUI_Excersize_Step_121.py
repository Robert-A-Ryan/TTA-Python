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

class ParentWindow(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self,master, *args, **kwargs)

        self.master=master
        self.master.minsize(480,170)
        self.master.maxsize(480,170)
        self.master.title('Check files')

        #form text boxes
        self.txtBrowse1 = tk.Entry(self.master,text='')
        self.txtBrowse1.grid(row=1,column=1,columnspan=3,padx=(30,0),pady=(40,0),ipadx=(99),ipady=(2),sticky=N+E)
        self.txtBrowse2 = tk.Entry(self.master,text='')
        self.txtBrowse2.grid(row=2,column=1,columnspan=3,padx=(30,0),pady=(10,0),ipadx=(99),ipady=(2),sticky=N+E)

        #buttons for the form
        self.btnBrowse1 = tk.Button(self.master,width=12,height=1,text='Browse...',)
        self.btnBrowse1.grid(row=1,column=0,padx=(15,0),pady=(40,0),sticky=N+E)
        self.btnBrowse2 = tk.Button(self.master,width=12,height=1,text='Browse...',)
        self.btnBrowse2.grid(row=2,column=0,padx=(15,0),pady=(10,10),sticky=N+E)
        self.btnCheckForFiles = tk.Button(self.master,width=12,height=1,text='Check for Files...')
        self.btnCheckForFiles.grid(row=3,column=0,padx=(15,0),pady=(0,10),ipady=(7),sticky=E)
        self.btnCloseProgram = tk.Button(self.master,width=12,height=1,text='Close Program')
        self.btnCloseProgram.grid(row=3, column=3,padx=(15,0),pady=(0,10),ipady=(7),sticky=E)


if __name__=='__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
