import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg')

#create a list with only the files in fileList that are txt files
filetxt = [i for i in (fileList)
    if str(fileList) and i.endswith('txt')]

#connect to db, create if necessary, and establish the cursor
conn = sqlite3.Connection('PythonCourseStep103.db')

#create a table in db
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tblMytxt( \
        fID INTEGER PRIMARY KEY AUTOINCREMENT, \
        colFlName TEXT \
        )')
    conn.commit()

#to add data to the db
with conn:
    cur = conn.cursor()
    for item in filetxt:
        cur.execute('INSERT INTO tblMytxt(colFlname) VALUES(?)', (item,))   
    conn.commit()

#query the table for the files and print them in a meaningful way
with conn:
    cur = conn.cursor()
    cur.execute('SELECT colFlName FROM tblMytxt')
    dtxt = cur.fetchall()
    for item in dtxt:
        print('\nFile Name: ' + str(item).strip("'(),"))
    
conn.close()
