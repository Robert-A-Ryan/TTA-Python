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
#My modules for this project
import phonebookGUI
import phonebookFunc

#Frame is the Tkinter frame class that our own class will iinherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)

        #define our master frame configuration
        self.master=master
        self.master.minsize(500,300) #window size Height, Width
        self.master.maxsize(500,300)
        #CenterWindow method will center the app on the users screen
        phonebookFunc.centerWindow(self,500,300)
        self.master.title('The Tkinter Phonebook Demo')
        self.master.configure(bg='#F0F0F0')
        #Tkinter built-in method of code to catch if user clicks on the X in the upper right corner in Windows
        self.master.protocol('WM_DELETE_WINDOW', lambda: phonebookFunc.askQuit(self))
        arg = self.master

        #load in the widgets from a separate module, to keep code compartmentalized
        phonebookGUI.loadGUI(self)







if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
