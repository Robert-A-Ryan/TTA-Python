#Python Ver:    3.7.5
#
#Author:        Robert Ryan
#               10-16-2019
#Purpose:       Phonebook Demo.  Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
#Tested OS:     Windows 10

#Importing modules needed for this project
import os
import sqlite3
import re
from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox
#My modules for this project
import phonebookMain
import phonebookGUI

def centerWindow(self,w,h): #pass the Tkinter frame(master) reference and the w and h
    #get the user's screen width and height
    screenWidth = self.master.winfo_screenwidth()
    screenHeight = self.master.winfo_screenheight()
    #calculate xy axis to paint the app in the center of the user's screen
    x = int((screenWidth/2)-(w/2))
    y = int((screenHeight/2)-(h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

#catch for the X in the upper right of the window
def askQuit(self):
    if messagebox.askokcancel('Exit Program', 'Okay to exit application?'):
        #closes app
        self.master.destroy()
        os._exit(0)

#database functions
def createDb(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE if not exists tblPhonebook(ID INTEGER PRIMARY KEY AUTOINCREMENT, colFname TEXT, colLname TEXT, colFullName TEXT,colPhone TEXT,colEmail TEXT)')
        #commit must be invoked to save changes and close the dB connection
        conn.commit()
    conn.close()
    firstRun(self)

def firstRun(self):
    data = ('John','Doe','John Doe','111-111-1111','jdoe@email.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = countRecords(cur)
        if count < 1:
            cur.execute('''INSERT INTO tblPhonebook(colFname,colLname,colFullName,colPhone,colEmail) VALUES(?,?,?,?,?)''',('John','Doe','John Doe','111-111-1111','jdoe@email.com'))
            conn.commit()
    conn.close()

def countRecords(cur):
    count = ''
    cur.execute('''SELECT COUNT(*) FROM tblPhonebook''')
    count = cur.fetchone()[0]
    return cur,count

#select item in listbox
def onSelect(self,event):
    #calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT colFname,ColLname,colPhone,colEmail FROM tblPhonebook WHERE colFullName = (?)''',[value])
        varBody = cursor.fetchall()
        #this returns a tuple to slice into 4 parts using data[] during iteration
        for data in varBody:
            self.txtFname.delete(0,END)
            self.txtFname.insert(0,data[0])
            self.txtLname.delete(0,END)
            self.txtLname.insert(0,data[1])
            self.txtPhone.delete(0,END)
            self.txtPhone.insert(0,data[2])
            self.txtEmail.delete(0,END)
            self.txtEmail.insert(0,data[3])

def addToList(self):
    varFname = self.txtFname.get()
    varLname = self.txtLname.get()
    #normalize the data for consistency
    #this will remove blank spaces before and after user's entry
    varFname = varFname.strip() 
    varLname = varLname.strip()
    #this will ensure that the first character in each word is capitalized
    varFname = varFname.title()
    varLname = varLname.title()
    #create the full name
    varFullName = ('{} {}'.format(varFname,varLname))
    print('varFullName: {}'.format(varFullName))
    varPhone = self.txtPhone.get().strip()
    #to check if phone number has correct form
    if chkPhone(varPhone) == False:
        varPhone = ''
    varEmail = self.txtEmail.get().strip()
    #to check email for correct format
    if chkEmail(varEmail) == False:
        varEmail = ''
    #force user to fill out form completely
    if (len(varFname) > 0) and (len(varLname) > 0) and (len(varPhone) > 0) and (len(varEmail) > 0):
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.cursor()
            #check to see if fullname matches the current database, if true alert user and disregard request
            cursor.execute("""SELECT COUNT(colFullName) FROM tblPhonebook WHERE colFullName = '{}'""".format(varFullName))
            count = cursor.fetchone()[0]
            chkName = count
            #check to see if there is an existance of the full name
            if chkName == 0:
                print('chkName: {}'.format(chkName))
                cursor.execute('''INSERT INTO tblPhonebook(colFname,colLname,colFullName,colPHone,colEmail) VALUES (?,?,?,?,?)''',(varFname,varLname,varFullName,varPhone,varEmail))
                #update listbox with new full name
                self.lstList1.insert(END,varFullName)
                #call function to clear all of the textboxes
                onClear(self)
            else:
                messagebox.showerror('Name Error','"{}" already exists in the database. Please choose a different name.'.format(varFullName))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror('Missing Text Error','Please ensure that you have completely filled out the form.')

def chkPhone(varPhone):
    regPhone = '^[0-9\-\+]{9,15}$'
    if not (re.search(regPhone,varPhone)):
        messagebox.showerror('Phone Format Error','The phone number you provided is not in a correct format.\n\nPlease resubmit a valid phone number')
        varPhone = ''
        return False

def chkEmail(varEmail):
    regEmail = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not (re.search(regEmail,varEmail)):
        messagebox.showerror('Email Format Error','The email you provided is not valid.\n\nPlease resubmit a valid email address')
        varEmail = ''
        return False

def onDelete(self):
    #get the listboxes selected value
    varSelect = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        #check count to ensure that this is not the last record in the database... cannot delete last recored or we will ge an error
        cur.execute('''SELECT COUNT(*) FROM tblPhonebook''')
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel('Delete Confirmation','All information associated with, ({}) \nwill be permenantly removed from the database. \n\nProceed with the deleteion request?'.format(varSelect))
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cursor=conn.cursor()
                    cursor.execute('''DELETE FROM tblPHonebook WHERE colFullName = "{}"'''.format(varSelect))
                #call the function to clear all of the textboxes and the selected index of listbox onRefresh(self) update the listbox with changes
                onDeleted(self)
                conn.commit()
        else:
            confirm = messagebox.showerror('Last Record Error', '({}) is the last record in the database and cannot be removed at this time. \n\nPlease add another record first before you can delete ({})'.format(varSelect,varSelect))
    conn.close()

def onDeleted(self):
    #clear the text in these textboxes
    self.txtFname.delete(0,END)
    self.txtLname.delete(0,END)
    self.txtPhone.delete(0,END)
    self.txtEmail.delete(0,END)
    #update the listbox onRefresh(self)
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    #clear the text in these textboxes
    self.txtFname.delete(0,END)
    self.txtLname.delete(0,END)
    self.txtPhone.delete(0,END)
    self.txtEmail.delete(0,END)

def onRefresh(self):
    #populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT COUNT(*) FROM tblPhonebook''')
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute('''SELECT colFullName FROM tblPhonebook''')
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i+1
    conn.close()

def onUpdate(self):
    try:
        #index of the list selection
        varSelect = self.lstList1.curselection()[0]
        #list selection text's value
        varValue = self.lstList1.get(varSelect)
    except:
        messagebox.showinfo('Missing Selection','No name was selected from the list.\nCancelling the Update request.')
        return
    #the user will only be able to update phone and email. for name changes the user will need to remove the entire record
    #normalized the data
    varPhone = self.txtPhone.get().strip()
    if chkPhone(varPhone) == False:
        varPhone = ''
    varEmail = self.txtEmail.get().strip()
    if chkEmail(varEmail) == False:
        varEmail = ''
    #ensure data entered
    if (len(varPhone) > 0) and (len(varEmail) > 0):
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            #count the records to see if the users's changes are already updated... meaning no changes needed
            cur.execute('''SELECT COUNT(colPhone) FROM tblPhonebook WHERE colPhone = "{}"'''.format(varPhone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute('''SELECT COUNT(colEmail) FROM tblPhonebook WHERE colEmail = "{}"'''.format(varEmail))
            count2 = cur.fetchone()[0]
            print(count2)
            #check to see if changes are not already made in the database
            if count == 0 or count2 == 0:
                response = messagebox.askokcancel('Update Request','The following changes ({}) and ({}) will be implemented for ({}).\n\nProceed with the update request?'.format(varPhone,varEmail,varValue))
                print(response)
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute('''UPDATE tblPhonebook SET colPhone = "{0}",colEmail = "{1}" WHERE colFullName = "{2}"'''.format(varPhone,varEmail,varValue))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo('Cancel Request', 'No changes have been made to ({}).'.format(varValue))
            else:
                messagebox.showinfo('No Changes Detected','Both ({}) and ({})\nalready exist in the database for this name.\n\nYour update request has been cancelled'.format(varPhone,varEmail))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror('Missing Information','Pleae select a name from the list.\nThen edit the phone or email information.')
    onClear(self)




if __name__ == "__main__":
    pass
