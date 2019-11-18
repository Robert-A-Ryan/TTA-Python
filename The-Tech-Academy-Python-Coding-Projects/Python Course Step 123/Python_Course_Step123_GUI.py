#Python Ver:    3.7.5
#
#Author:        Robert Ryan
#               10-17-2019
#
#Purpose:       Python Course Step 123 Project
#               Using Python, Tkinter , Shutil and os to build an application 
#               that will iterate through a directory, select the .txt files 
#               and move them to a different directory
#
#Tested OS:     Windows 10

#Importing modules needed for this project
import os
from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox
#My modules for this project
import Python_Course_Step123_Main
import Python_Course_Step123_Func

def loadGUI(self):

    #form labels
    self.lblAppDesc = tk.Label(self.master,text='Enter the type of file(s) you would like to move.')
    self.lblAppDesc.grid(row=0,column=0,columnspan=6,padx=(10,0),pady=(10,0),sticky=N+W)
    self.lblFileType = tk.Label(self.master,text='File Extension Type:')
    self.lblFileType.grid(row=1,column=0,padx=(10,75),pady=(10,0),sticky=N+W)
    self.lblRelo = tk.Label(self.master,text='Files to be relocated.')
    self.lblRelo.grid(row=0,column=6,columnspan=2,padx=(10,0),pady=(10,0),sticky=S+W)
    self.lblSource = tk.Label(self.master,text='Source Directory:')
    self.lblSource.grid(row=2,column=0,columnspan=5,padx=(10,0),pady=(15,0),sticky=N+W)
    self.lblDest = tk.Label(self.master,text='Destination Directory:')
    self.lblDest.grid(row=4,column=0,columnspan=5,padx=(10,0),pady=(15,0),sticky=N+W)

    #form buttons
    self.btnSource = tk.Button(self.master,width=10,height=1,text='Browse...',command=lambda:Python_Course_Step123_Func.selectSourceDir(self))
    self.btnSource.grid(row=3,column=5,padx=(10,0),pady=(3,0),sticky=N+W)
    self.btnDest = tk.Button(self.master,width=10,height=1,text='Browse...',command=lambda:Python_Course_Step123_Func.selectDestDir(self))
    self.btnDest.grid(row=5,column=5,padx=(10,0),pady=(3,0),sticky=N+W)
    self.btnFind = tk.Button(self.master,width=10,height=2,text='Find Files',command=lambda:Python_Course_Step123_Func.findFiles(self))
    self.btnFind.grid(row=6,column=0,padx=(15,0),pady=(10,10),sticky=N+W)
    self.btnMove = tk.Button(self.master,width=10,height=2,text='Move Files',command=lambda:Python_Course_Step123_Func.moveFiles(self))
    self.btnMove.grid(row=6,column=0,padx=(100,0),pady=(10,10),sticky=N+W)
    self.btnClear = tk.Button(self.master,width=10,height=2,text='Clear Form',command=lambda:Python_Course_Step123_Func.clearForm(self))
    self.btnClear.grid(row=6,column=6,padx=(0,75),pady=(10,10),sticky=N+E)   
    self.btnCancel = tk.Button(self.master,width=10,height=2,text='Cancel',command=lambda:Python_Course_Step123_Func.askQuit(self))
    self.btnCancel.grid(row=6,column=6,columnspan=2,padx=(0,10),pady=(10,10),sticky=N+E)

    #form textboxes
    self.txtFileType = tk.Entry(self.master,text='',width=10)
    self.txtFileType.focus()
    self.txtFileType.grid(row=1,column=0,padx=(125,0),pady=(12,0),ipady=(2),sticky=N+W)
    self.txtSource = tk.Entry(self.master,text='',width=60)
    self.txtSource.grid(row=3,column=0,columnspan=5,padx=(10,0),pady=(5,0),ipady=(2),sticky=N+W)
    self.txtDest = tk.Entry(self.master,text='',width=60)
    self.txtDest.grid(row=5,column=0,columnspan=5,padx=(10,0),pady=(5,0),ipady=(2),sticky=N+W)

    #listbox with scrollbar
    self.scrollbar = Scrollbar(self.master,orient=VERTICAL)
    self.lstFiles = Listbox(self.master,exportselection=0,width=30,yscrollcommand=self.scrollbar.set)
    #self.lstFiles.bind('<<ListboxSelect>>',lambda event: Python_Course_Step123_Func.onFind(self,event))
    self.scrollbar.config(command=self.lstFiles.yview)
    self.scrollbar.grid(row=1,column=7,rowspan=5,padx=(5,0),pady=(0,0),sticky=N+E+S)
    self.lstFiles.grid(row=1,column=6,rowspan=5,padx=(10,0),pady=(12,0),sticky=N+E+S+W)

    #Python_Course_Step123_Func.createDb(self)
    #Python_Course_Step123_Func.onRefresh(self)

if __name__=='__main__':
    pass