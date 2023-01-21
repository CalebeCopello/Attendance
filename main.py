#Importing modules
import sqlite3 as sql


#Functions
def insertName(lN, n):
    dbcursor.execute('INSERT INTO members (lastName, name) VALUES (?, ?)', (lN, n))
    connection.commit()
def addAttRate(attRate, rowId):
    dbcursor.execute('UPDATE members SET attRate = ? WHERE rowid= ?', (attRate, rowId))
    connection.commit()
def listAllMembers():
    dbcursor.execute('SELECT rowid, lastName, Name, attRate FROM members')
    result = dbcursor.fetchall()
    for result in result:
        print(result)
def deleteMember(rowId):
    dbcursor.execute('DELETE FROM members WHERE rowid = ?', (rowId))
    connection.commit()

#Connecting to db and creating a cursor
connection = sql.connect('general.db')
dbcursor = connection.cursor()

#Creating the table if not exists
try:
    dbcursor.execute('CREATE TABLE members (lastName TEXT, name TEXT, attRate INTEGER)')
    connection.commit()
except sql.Error as problem:
    #print(problem)
    pass

#insertName('Copello', 'Verônica Isis Bortolossi Rodrigues')
#addAttRate(15,4)
#deleteMember('3')

#TODO make an function to reorder rowids after deleting one row, using commando below as guide
#dbcursor.execute('UPDATE members SET rowid = {newRowId} WHERE rowid = {oldRowId}')

listAllMembers()

#Closing DB connection
connection.close()
