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
import os
import sqlite3
import time
import shutil
from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.constants as constants, tkinter.filedialog as filedialog
#My modules for this project
import Python_Course_Step123_Main
import Python_Course_Step123_GUI

#to center GUI on the user's screen
def centerWindow(self,w,h):
    screenWidth = self.master.winfo_screenwidth()
    screenHeight = self.master.winfo_screenheight()
    x = int((screenWidth/2)-(w/2))
    y = int((screenHeight/2)-(h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

def askQuit(self):
    if messagebox.askokcancel('Exit Program', 'Okay to exit application?'):  
        self.master.destroy()
        os._exit(0)

#database functions
def createDb(mergedList,desPath):
    conn = sqlite3.connect('filemove.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE if not exists tblFileMove(colID INTEGER PRIMARY KEY AUTOINCREMENT, colFileName TEXT, colTimeStamp TEXT)')
        conn.commit()
    conn.close()
    recordFile(mergedList)

def recordFile(mergedList):
    conn = sqlite3.connect('filemove.db')
    with conn:
        cur = conn.cursor()
        cur.executemany('INSERT INTO tblFileMove(colFileName,colTimeStamp) VALUES (?,?)',mergedList)
        conn.commit()
    conn.close()

#choosing the source directory
def selectSourceDir(self):
    dirPath = filedialog.askdirectory()
    if dirPath:
        self.txtSource.delete(0,END)
        self.txtSource.insert(0,dirPath)

#choosing the destination directory
def selectDestDir(self):
    dirPath = filedialog.askdirectory()
    if dirPath:
        self.txtDest.delete(0,END)
        self.txtDest.insert(0,dirPath)

#finding the files that we want to move
def findFiles(self):
    varSource = self.txtSource.get()
    varDest = self.txtDest.get()
    varFileType = self.txtFileType.get()
    fileName = []
    #normalize the input so the app knows how to use the file type
    varFileType = varFileType.strip(' .')
    #require entry into txtFileType, Source Dir and Destination Dir
    if not (len(varFileType) > 0 and (len(varSource) > 0 and (len(varDest) > 0))):
        messagebox.showerror('Missing Information','Make sure you have selected a Source Directory, Destination Directory and File Type')
    else:
        fileName = chkForFile(fileName,varSource,varFileType)
        self.lstFiles.delete(0,END)
        for item in fileName:
            self.lstFiles.insert(0,item)

#check for files matching the type requested in the source directory
def chkForFile(fileName,varSource,varFileType):
    srcPath = varSource
    ext = varFileType
    fileName = [i for i in os.listdir(srcPath) if os.path.isfile(os.path.join(srcPath,i)) and i.endswith(ext)]
    return fileName

def moveFiles(self):
    #grab the current files in lstFiles and move them to the dest directory
    fileName = self.lstFiles.get(0,END)
    ext = self.txtFileType.get()
    srcPath = self.txtSource.get()
    desPath = self.txtDest.get()
    finPath = [srcPath + '/' + i for i in fileName]
    i = 0
    while i < len(finPath):
        shutil.move(finPath[i],desPath)
        i += 1
    chkFileTime(fileName,desPath)
    clearForm(self)
    
def clearForm(self):
    self.lstFiles.delete(0,END)
    self.txtFileType.delete(0,END)
    self.txtSource.delete(0,END)
    self.txtDest.delete(0,END)

def chkFileTime(fileName,desPath):
    #grab the current time stamp on filename to add to database
    fileWTime = []
    for i in range(len(fileName)):
        pthTime=((time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getmtime(os.path.join(desPath, str(fileName[i])))))))
        fileWTime.append(pthTime)
    merge(fileName,fileWTime,desPath)

def merge(fileName,fileWTime,desPath):
    #merge fileName and fileWTime into mergedList
    mergedList = [(fileName[i], fileWTime[i])for i in range(0,len(fileName))]
    print(mergedList)
    createDb(mergedList,desPath)







if __name__ == '__main__':
    pass