import sqlite3
class DatabaseManager():
    def __init__(self):
        self.connection = sqlite3.connect("library.db", isolation_level=None)
        self.cur = self.connection.cursor()
    
    def close(self):
        self.cursor.close()
        self.connection.close()

