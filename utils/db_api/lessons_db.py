import sqlite3 as sql


class Lessons:

    def __init__(self, database: str) -> None:
        self.conn = sql.connect(database, check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_lessons(self) -> None:
        query: str = ("""
                CREATE TABLE IF NOT EXISTS "LESSONS" (
                "ID"	INTEGER PRIMARY KEY,
                "NUM_LESSONS"	INTEGER,
                "NAME" TEXT,
                "FORMAT"	TEXT,
                "TIME_START"	TEXT,
                "TIME_END"	TEXT,
                "CABINET"	TEXT,
                "LESSON_ID" INTEGER NOT NULL,
                FOREIGN KEY("LESSON_ID") REFERENCES timetable("ID"));
                """)

        self.cur.execute(query)
        self.conn.commit()

    def get_shedule(self, weekday: int) -> list:
        query: str = f"""
                SELECT *
                FROM "LESSONS"
                WHERE LESSON_ID = {weekday}
            """

        self.cur.execute(query)
        return self.cur.fetchall()
