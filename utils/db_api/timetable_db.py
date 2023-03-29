import sqlite3 as sql
from typing import Any


class Timetable:

    def __init__(self, database: str) -> None:
        self.conn = sql.connect(database, check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_timetable(self) -> None:
        query: str = ("""
                CREATE TABLE IF NOT EXISTS "timetable" (
                "ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
                "WEEK"	TEXT NOT NULL);
                """)

        self.cur.execute(query)
        self.conn.commit()

    def get_weekday(self, weekday: int) -> list:
        query: str = f"""
            SELECT *
            FROM "timetable"
            WHERE ID = {weekday}
        """

        return self.cur.execute(query).fetchone()

    def get_day(self) -> Any:
        query: str = """
            SELECT nuday
            FROM numday
            WHERE ID = 1
        """

        return self.cur.execute(query).fetchone()

    def next_day(self) -> None:
        numday: int = self.get_day()[0]
        queru: str = """UPDATE numday SET nuday = ?"""
        if numday >= 14:
            numday = 1
        if numday < 14:
            numday = numday + 1

        self.cur.execute(queru, numday)
        self.conn.commit()
