#Python Ver:    3.7.5
#
#Author:        Robert Ryan
#               10-17-2019
#
#Purpose:       Python Course Step 123 Project
#               Using Python, Tkinter and os to build an application that 
#               will iterate through a directory, select the .txt files 
#               and move them to a different directory
#
#Tested OS:     Windows 10

#Importing modules needed for this project

from tkinter import *
import tkinter as tk
#My modules for this project
import Python_Course_Step123_GUI
import Python_Course_Step123_Func

#setting up the tkinter frame class for our GUI
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our MWindow Frame configuration
        self.master=master
        self.master.minsize(690,275)
        self.master.maxsize(690,275)
        #CenterWindow method will center the GUI on the users screen
        Python_Course_Step123_Func.centerWindow(self,500,500)
        self.master.title('File Relocation Application')
        #to catch if user selects the X in the upper right
        self.master.protocol('WM_DELETE_WINDOW', lambda:Python_Course_Step123_Func.askQuit(self))
        arg = self.master

        #load in the widgets from a separate module
        Python_Course_Step123_GUI.loadGUI(self)


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()