import sqlite3
connection = sqlite3.connect('corona.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute('SELECT * FROM Confirmed')
row = cursor.fetchone()
id = row['field2']
print(id)
