import sqlite3


class DB:
    def __init__(self):
        self.connection = sqlite3.connect('../identifier.sqlite')

    def store(self, data):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO events VALUES(?,?,?)', data)
        self.connection.commit()

    def read(self, data: list):
        band, city, date = data
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
        cursor.fetchall()
