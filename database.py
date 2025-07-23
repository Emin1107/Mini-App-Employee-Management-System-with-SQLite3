import sqlite3

def createTable():
    base = sqlite3.connect('Radnici.db')
    cursor = base.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Radnici (
                   id TEXT PRIMARY KEY,
                   name TEXT,
                   nachname TEXT,
                   jahre INT,
                   status TEXT)
                   ''')
    base.commit()
    base.close()

def fetchEmployees():
    base = sqlite3.connect('Radnici.db')
    cursor = base.cursor()
    cursor.execute('SELECT * FROM Radnici')
    employees = cursor.fetchall()
    base.close()
    return employees

def insertEmployees(id, name, nachname, jahre, status):
    base = sqlite3.connect('Radnici.db')
    cursor = base.cursor()
    cursor.execute('INSERT INTO Radnici (id, name, nachname, jahre, status) VALUES (?, ?, ?, ?, ?)',
                  (id, name, nachname, jahre, status))
    base.commit()
    base.close()

def updateEmployees(neuName, neuNachname, neuJahre, neuStatus, id):
    base = sqlite3.connect('Radnici.db')
    cursor = base.cursor()
    cursor.execute('UPDATE Radnici SET name = ?, nachname = ?, jahre = ?, status = ? WHERE id = ?',
                   (neuName, neuNachname, neuJahre, neuStatus, id))
    base.commit()
    base.close()

def deleteEmployees(id):
    base = sqlite3.connect('Radnici.db')
    cursor = base.cursor()
    cursor.execute('DELETE FROM Radnici WHERE id = ?', (id,))
    base.commit()
    base.close()

def idExistent(id):
    base = sqlite3.connect('Radnici.db')
    cursor = base.cursor()
    cursor.execute('SELECT COUNT(*) FROM Radnici WHERE id = ?', (id,))
    result = cursor.fetchone()
    base.close()
    return result[0] > 0

createTable()