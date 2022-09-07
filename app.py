from flask import Flask, render_template, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
app.config["SECRET_KEY"] = "MatthewMichaelMattMurdock"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    done = db.Column(db.Boolean, default=False)


def username_not_used(username):
    if User.query.filter_by(username=username.data).first():
        flash("Username already in use", "danger")
        raise ValidationError("Username already exists.")


class RegisterForm(FlaskForm):
    username = StringField(
        validators=[lambda form, username: username_not_used(username)],
        render_kw={
            "placeholder": "Username",
            "class": "form-control mt-3 mb-1"
        })
    password = PasswordField(
        render_kw={
            "placeholder": "Password",
            "class": "form-control mt-1 mb-1"
        })
    confirm_password = PasswordField(
        render_kw={
            "placeholder": "Confirm password",
            "class": "form-control mt-1 mb-3"
        })
    submit = SubmitField("Register", render_kw={
        "class": "btn btn-dark mt-3 mb-3"
    })


class LoginForm(FlaskForm):
    username = StringField(
        render_kw={
            "placeholder": "Username",
            "class": "form-control mt-3 mb-1"
        })
    password = PasswordField(
        render_kw={
            "placeholder": "Password",
            "class": "form-control mt-1 mb-3"
        })
    submit = SubmitField("Log in", render_kw={
        "class": "btn btn-dark mt-3 mb-3"
    })


class TaskAddForm(FlaskForm):
    task = StringField(
        render_kw={
            "placeholder": "Task title",
            "class": "form-control"
        })
    submit = SubmitField("Add task", render_kw={
        "class": "btn btn-outline-dark"
    })


@app.route('/toggle/<taskid>')
def toggle(taskid):
    task = Task.query.get(taskid)
    task.done = not task.done
    db.session.commit()
    return '', 204


@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    else:
        return render_template("home.html")


@app.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
    form = TaskAddForm()
    tasks = current_user.tasks

    if form.validate_on_submit():
        if not form.task.data:
            flash("Missing task title", "danger")
            return render_template("dashboard.html", tasks=tasks, form=form)

        task = Task()
        task.title = form.task.data
        task.user_id = current_user.id
        db.session.add(task)
        db.session.commit()
        flash(f"New task added: {form.task.data}", "success")
        return redirect(url_for("dashboard"))

    return render_template("dashboard.html", tasks=tasks, form=form)


@app.route('/logout', methods=["GET", "POST"])
def logout():
    logout_user()
    flash("Logged out", "primary")
    return redirect(url_for("home"))


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if not form.username.data:
            flash("Missing username", "danger")
            return render_template("login.html", form=form)

        if not form.password.data:
            flash("Missing password", "danger")
            return render_template("login.html", form=form)

        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("Logged in successfully", "success")
                return redirect(url_for("dashboard"))
            else:
                flash("Incorrect username or password", "danger")
                return render_template("login.html", form=form)
        else:
            flash("Incorrect username or password", "danger")
            return render_template("login.html", form=form)
    return render_template("login.html", form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        if not form.username.data:
            flash("Missing username", "danger")
            return render_template("register.html", form=form)

        if not form.password.data:
            flash("Missing password", "danger")
            return render_template("register.html", form=form)

        if not form.confirm_password.data:
            flash("Missing password confirmation", "danger")
            return render_template("register.html", form=form)

        if form.password.data != form.confirm_password.data:
            flash("Confirmed password doesn't match password", "danger")
            return render_template("register.html", form=form)

        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User()
        new_user.username = form.username.data
        new_user.password = hashed_password
        db.session.add(new_user)
        db.session.commit()
        flash('Registered successfully', "success")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
