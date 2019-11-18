#
# Python:   3.7.5
#
# Author:   Robert Ryan (coachrobertryan@gmail.com)
#
#Purpose:   To search a file path on computer and test for .txt files and
#           return the last time the files were updated.
#           


import os
import time

filePth = os.getcwd()
ext = 'txt'

def checkFortxt():
    #check the directory for all files ending in .txt
    #and creating a list (fileName) from these files
    fileName = [i for i in os.listdir(filePth)
        if os.path.isfile(os.path.join(filePth, i))
        and i.endswith(ext)]
    
    checkTme(fileName)
        
    


def checkTme(fileName):
    #Print a sentence showing the file name and when it was last modified.
    for i in range(len(fileName)):
        print('\nThe file ' + fileName[i] + ' was last modfied at '
        + (time.strftime('%Y-%m-%d %H:%M:%S',
        time.localtime(os.path.getmtime
        (os.path.join(filePth, str(fileName[i])))))))
   

if __name__ == '__main__':
    checkFortxt()
