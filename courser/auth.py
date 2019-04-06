from flask import (
    Blueprint, render_template, request, redirect, url_for, g, flash, session
)
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

from .db import query_db, get_db


auth = Blueprint('auth', __name__, url_prefix='/auth')


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])


@auth.route('/register', methods=('GET', 'POST'))
def register():
    form = LoginForm()
    if form.validate_on_submit():
        db = get_db()
        # insert the new user into the database
        error = None

        username = form.username.data
        password = form.password.data

        user = db.execute("SELECT id FROM User WHERE username = ?", [username]).fetchone()
        if user is not None:
            error = 'User {} is already registered'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO User (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = query_db('select * from user where username = ?', [form.username], one=True)
        error = None
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], form.password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('dashboard'))

        flash(error)

    return render_template('auth/login.html', form=form)


def required_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if get_current_user_role() not in roles:
                flash('Authentication error, please try again.', 'error')
                return redirect(url_for('dashboard'))
            return f(*args, **kwargs)
        return wrapped
    return wrapper


def login_required(view):
    @wraps(view)
    def wrapped(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))


def get_current_user_role():
    return g.user.role

