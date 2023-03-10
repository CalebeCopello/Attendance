#Importing modules
import sqlite3 as sql


#Functions
#Connecting to db and creating a cursor
def sqlOpen():
    global connection
    global dbcursor
    connection = sql.connect('general.db')
    dbcursor = connection.cursor()

def insertName(lN, n):
    dbcursor.execute('INSERT INTO members (lastName, name) VALUES (?, ?)', (lN, n))
    connection.commit()
def addAttRate(attRate, rowId):
    dbcursor.execute('UPDATE members SET att = ? WHERE rowid= ?', (attRate, rowId))
    connection.commit()
def listAllMembers():
    dbcursor.execute('SELECT rowid, lastName, Name, att FROM members')
    result = dbcursor.fetchall()
    #for result in result:
    return result
def deleteMember(rowId):
    dbcursor.execute('DELETE FROM members WHERE rowid = ?', (rowId))
    connection.commit()


sqlOpen()

#Creating the table if not exists
try:
    dbcursor.execute('CREATE TABLE members (lastName TEXT, name TEXT, att INTEGER)')
    connection.commit()
except sql.Error as problem:
    #print(problem)
    pass

#Feeding Table
"""
insertName('Monteiro', 'Alan Jonathan Farias Costa')
insertName('Mobley', 'Elder')
insertName('Rodrigues', 'Isadora Cristina Bortolossi')
insertName('Copello', 'Calebe Soares')
insertName('Copello', 'Verônica Isis Bortolossi Rodrigues')
insertName('de Marchi', 'Felipe Oliveira ')
insertName('Fernandes', 'Ronaldo dos Santos')
insertName('Alves', 'Maickel Lima')
insertName('Barros', 'Aurora Lima da Silva')
insertName('Lima', 'Bryan Paim')
"""

#addAttRate(15,4)
#deleteMember('2')


#TODO make an function to reorder rowids after deleting one row, using commando below as guide
#dbcursor.execute('UPDATE members SET rowid = {newRowId} WHERE rowid = {oldRowId}')

'''member = listAllMembers()
c = 0
while c < len(member):
    i = 0
    while i < len(member[c]):
        print(member[c][i])
        i += 1
    c += 1'''

#Closing DB connection
connection.close()
