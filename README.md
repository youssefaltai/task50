# CS50 Final Project

## Requirements

- Install Python 3.x
- Install SQLite3

## Setting up the environment

1. Open a terminal window, run the following command to clone the
   repository `git clone https://github.com/youssef-attai/cs50_project.git`
2. `cd` to the directory `cs50_project`
3. If you don't already have virtualenv installed, run the following command `pip3 install virtualenv`
4. Run `virtualenv venv` to create a new environment called "venv"
5. Run `source venv/bin/activate` to activate the virtual environment
6. Run `pip3 install -r requirements.txt` to install the requirements in the environment

## Setting up the database

1. Open a terminal window, and `cd` to the directory containing `app.py`
2. Run the following command `touch database.db`
3. Run the Python console typing `python` or `python3` and hitting Enter
4. Type `from app import db` and hit Enter
5. Type `db.create_all()` and hit Enter
6. Type `exit()` and hit Enter to exit the Python console
7. Make sure the database is created successfully by running `sqlite3 database.db .tables`, you should see `user`
