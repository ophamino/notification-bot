from .timetable_db import Timetable
from .users_db import Users
from .lessons_db import Lessons
from .photo_db import Photo


db_timetable = Timetable('chat.db')
db_users = Users('chat.db')
db_lessons = Lessons('chat.db')
db_photo = Photo('chat.db')


def db_start() -> None:
    db_lessons.create_lessons()
    db_timetable.create_timetable()
    db_users.create_users()
    db_photo.create_photo_table()
