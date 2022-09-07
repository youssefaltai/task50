# Task50

![Screenshot of the app's dashboard](https://github.com/youssef-attai/cs50_project/blob/master/imgs/screenshot.png)

This is my CS50's Final Project, it is a To-do web app created using Flask and Bootstrap. You can sign up for a new
account.
You can create, edit and delete tasks, and of course, mark them as done.

You can either start using the app by clicking [here](http://task50.herokuapp.com/),

or walk through the steps below to run the app locally on your machine.

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

1. Run the following command `touch database.db`
2. Run the following command `export DATABASE_URL=sqlite:///database.db`
3. Run the Python console typing `python` or `python3` and hitting Enter
4. Type `from app import db` and hit Enter
5. Type `db.create_all()` and hit Enter
6. Type `exit()` and hit Enter to exit the Python console
7. Make sure the database is created successfully by running `sqlite3 database.db .tables`, you should see two
   tables, `user` and `task`

## Running the app

1. Run the following command `flask run`
2. Go to http://127.0.0.1:5000, you should see the app working as expected

## Existing the app

1. Just hit CTRL+C in the terminal window

## How everything works

### Entity-Relationship Diagram

![ER Diagram](https://github.com/youssef-attai/cs50_project/blob/master/imgs/erd.png)

### Technologies used

- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
- [JQuery](https://jquery.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

Authentication is done using [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

Database management is done using [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

Password hashing is done using [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/1.0.1/)

HTML forms are done using [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/)

Icons are from [FontAwesome](https://fontawesome.com/)

### Acknowledgments

- [Stackoverflow answer by Hosein Yeganloo](https://stackoverflow.com/a/44724510/14174934)
- [Stackoverflow answer by Erwin Brandstetter](https://stackoverflow.com/a/11919677/14174934)
- [Stackoverflow answer by Leandro Lima and davidism](https://stackoverflow.com/a/64698899/14174934)
- [Stackoverflow answer by FogleBird and tremendows](https://stackoverflow.com/a/7478705/14174934)
- [Heroku Dev Center - Setting up Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#set-up-postgres-on-linux)
- [Real Python YouTube Video - Deploy a Flask Application on Heroku](https://www.youtube.com/watch?v=4_EO4RwABbA)
- [Codemy.com YouTube Video - Deploy Flask App With Database On Heroku](https://www.youtube.com/watch?v=SiCAIRc0pEI)