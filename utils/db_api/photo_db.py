import sqlite3 as sql


class Photo:

    def __init__(self, database: str) -> None:
        self.conn = sql.connect(database, check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_photo_table(self) -> None:
        query: str = ("""
                CREATE TABLE IF NOT EXISTS `photo_table` (
                `id`	INTEGER PRIMARY KEY AUTOINCREMENT,
                `photo`	TEXT NOT NULL);
                """)

        self.cur.execute(query)
        self.conn.commit()

    def add_photo(self, photo_id: str) -> None:
        query: str = ("""INSERT INTO `photo_table` (photo) VALUES(?)""")
        self.cur.execute(query, (photo_id, ))
        self.conn.commit()

    def get_photo(self) -> list:
        query: str = ("""SELECT `photo` FROM `photo_table`""")
        return self.cur.execute(query).fetchall()
