from flask import (
    Blueprint, render_template, request
)

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    return render_template('auth/login.html')
