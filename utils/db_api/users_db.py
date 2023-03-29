import sqlite3 as sql
from typing import Tuple, Union, Any


class Users:

    def __init__(self, database: str) -> None:
        self.conn = sql.connect(database, check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_users(self) -> None:
        query: str = ("""
                      CREATE TABLE IF NOT EXISTS "users"(
                      "TG_ID" INTEGER PRIMARY KEY,
                      "USERNAME" TEXT,
                      "FIRST_NAME" TEXT,
                      "ACTIVE" INTEGER DEFAULT 1);
                      """)

        self.cur.execute(query)
        self.conn.commit()

    def user_exists(self, tg_id: int) -> bool:
        with self.conn:
            result: list[int] = self.cur.execute(f"""
                                      SELECT TG_ID
                                      FROM users
                                      WHERE TG_ID = {tg_id};
                                      """).fetchmany(1)

            return bool(len(result))

    def add_user(self, tg_id: int, username: Union[str, None, Any], first_name: str) -> None:
        values: Tuple[int, Union[str, Any], str, int] = (tg_id, username, first_name, 1)
        query: str = ("""INSERT INTO "users" VALUES(?, ?, ?, ?)""")

        self.cur.execute(query, values)
        self.conn.commit()

    def get_all_users(self) -> list:
        query: str = ("SELECT TG_ID FROM users")

        return self.cur.execute(query).fetchall()
