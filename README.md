# CS50 Final Project

## Requirements
- Install Python 3.x
- Install SQLite3

1. Open a terminal window, and `cd` to the directory containing `app.py`
2. Run the following command `touch database.db`
3. Run the Python console using `python` or `python3`
4. Type `from app import db` and hit Enter
5. Type `db.create_all()` and hit Enter
6. Type `exit()` and hit Enter to exit the Python console
7. Make sure the database is created successfully by running `sqlite3 database.db .tables`, you should see `user`