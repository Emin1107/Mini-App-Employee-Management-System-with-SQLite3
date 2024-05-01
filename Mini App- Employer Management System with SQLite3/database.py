import sqlite3

def createTable():
    base = sqlite3.connect('Workers.db')
    cur = base.cursor()

    cur.execute('''
                CREATE TABLE IF NOT EXISTS Workers 
                (
                id TEXT PRIMARY KEY,
                name TEXT,
                teilnehmer_ID TEXT,
                benutzer_ID TEXT,
                pin TEXT,
                svnr TEXT,
                status TEXT,
                geld INT,
                details TEXT
                )
                ''')
    base.commit()
    base.close()

def fetchWorker():
    base = sqlite3.connect('Workers.db')
    cur = base.cursor()

    cur.execute('SELECT * FROM Workers')
    worker = cur.fetchall()
    base.close()
    return worker

def insertWorker(id, name, teilnehmer_ID, benutzer_ID, pin, svnr, status, geld, details):
    base = sqlite3.connect('Workers.db')
    cur = base.cursor()

    cur.execute('INSERT INTO Workers (id, name, teilnehmer_ID, benutzer_ID, pin, svnr, status, geld, details) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                (id, name, teilnehmer_ID, benutzer_ID, pin, svnr, status, geld, details))
    base.commit()
    base.close()

def updateWorker(neuName, neuTeilnehmer_ID, neuBenutzer_ID, neuPin, neuSvnr, neuStatus, neuGeld, neuDetails, id):
    base = sqlite3.connect('Workers.db')
    cur = base.cursor()

    cur.execute('UPDATE Workers SET name = ?, teilnehmer_ID = ?, benutzer_ID = ?, pin = ?, svnr = ?, status = ?, geld = ?, details = ? WHERE id = ?',
                (neuName, neuTeilnehmer_ID, neuBenutzer_ID, neuPin, neuSvnr, neuStatus, neuGeld, neuDetails, id))
    base.commit()
    base.close()

def deleteWorker(id):
    base = sqlite3.connect('Workers.db')
    cur = base.cursor()

    cur.execute('DELETE FROM Workers WHERE id = ?', (id,))
    base.commit()
    base.close()

def idExists(id):
    base = sqlite3.connect('Workers.db')
    cur = base.cursor()

    cur.execute('SELECT COUNT(*) FROM Workers WHERE id = ?', (id,))
    rez = cur.fetchone()
    base.close()
    return rez[0] > 0

def countGeld():
    base = sqlite3.connect('Workers.db')
    cur = base.cursor()

    cur.execute('SELECT SUM(Geld) FROM Workers')
    rez = cur.fetchone()
    base.close()
    return rez[0] > 0

createTable()