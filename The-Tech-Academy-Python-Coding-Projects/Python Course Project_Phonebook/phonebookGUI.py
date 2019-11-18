#Python Ver:    3.7.5
#
#Author:        Robert Ryan
#               10-16-2019
#Purpose:       Phonebook Demo.  Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
#Tested OS:     Windows 10

#Importing modules needed for this project
from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox
#My modules for this project
import phonebookMain
import phonebookFunc


def loadGUI(self):

    #form labels
    self.lblFname = tk.Label(self.master,text='First Name:')
    self.lblFname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lblLname = tk.Label(self.master,text='Last Name:')
    self.lblLname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lblPhone = tk.Label(self.master,text='Phone Number:')
    self.lblPhone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lblEmail = tk.Label(self.master,text='Email:')
    self.lblEmail.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lblUser = tk.Label(self.master,text='Contact:')
    self.lblUser.grid(row=0,column=2,padx=(0,0),pady=(10,0),sticky=N+W)

    #form text boxes
    self.txtFname = tk.Entry(self.master,text='')
    self.txtFname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txtLname = tk.Entry(self.master,text='')
    self.txtLname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txtPhone = tk.Entry(self.master,text='')
    self.txtPhone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txtEmail = tk.Entry(self.master,text='')
    self.txtEmail.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    #listbox with scroll bar
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>',lambda event: phonebookFunc.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    #buttons for the form
    self.btnAdd = tk.Button(self.master,width=12,height=2,text='Add',command=lambda:phonebookFunc.addToList(self))
    self.btnAdd.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btnUpdate = tk.Button(self.master,width=12,height=2,text='Update',command=lambda:phonebookFunc.onUpdate(self))
    self.btnUpdate.grid(row=8,column=1,padx=(15,0),pady=(45,10),sticky=W)
    self.btnDelete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda:phonebookFunc.onDelete(self))
    self.btnDelete.grid(row=8, column=2,padx=(15,0),pady=(45,10),sticky=W)
    self.btnClose = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: phonebookFunc.askQuit(self))
    self.btnClose.grid(row=8,column=4,padx=(15,0),pady=(45,10),sticky=E)

    #
    phonebookFunc.createDb(self)
    phonebookFunc.onRefresh(self)






if __name__=='__main__':
    pass
