import sqlite3
connection = sqlite3.connect('test.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

#cursor.execute('CREATE TABLE names (id INTEGER PRIMARY KEY, name TEXT)')

#cursor.execute('INSERT INTO names VALUES(?, ?)',(1,'DONALD'))

#cursor.execute('INSERT INTO names(name) VALUES(?)',('Richard',))

#cursor.execute('INSERT INTO names VALUES(?,?)', (3, 'Agnes'))
connection.rollback()
#cursor.execute('INSERT INTO names VALUES(?,?)',(4,'Ben'))

cursor.execute('SELECT *  FROM names')
row = cursor.fetchone()
id = row['id']
name = row['name']
print('id: ' + str(id))
print('name: ' + str(name))

connection.commit()
