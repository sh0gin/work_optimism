import sqlite3

class Db:
    def __init__(self):
        self.connection = sqlite3.connect("pypropj.db")
        self.connection.row_factory = sqlite3.Row

    def query(self, sql, params={}, cls=''):
        cursor = self.connection.cursor()
        rows = cursor.execute(sql, params).fetchall()
        items = []
        for row in rows:
            item = dict(row)
            items.append(dict())
        return items