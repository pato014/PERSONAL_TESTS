import sqlite3

CONNECTION = sqlite3.connect('../identifier.sqlite')

def db_operations(data):
    conn = CONNECTION
    cursor = conn.cursor()
    cursor.execute('INSERT INTO events VALUES(?,?,?)', data)
    conn.commit()
