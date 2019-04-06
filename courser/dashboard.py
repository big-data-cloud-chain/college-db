from flask import (
    Blueprint, render_template, g, redirect, url_for, request, flash, session
)

from werkzeug.exceptions import abort

from .db import query_db, get_db
from .auth import login_required


dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
def index():
    user_id = session.get('user_id')
    if user_id is None:
        flash("Must be logged in")
        return redirect(url_for('auth.login'))

    grades = get_grades(user_id)
    if grades is not None:
        session['user_grades'] = grades

    return render_template('dashboard/index.html')


def get_grades(id):
    grades = get_db().execute(
        'SELECT en.grade FROM Enrolment AS en '
        'INNER JOIN Section AS sec '
        'ON en.section_id = sec.id '
        'INNER JOIN Course AS co '
        'ON sec.course_id = co.id '
        'WHERE en.student_id=? ', (id,)
    ).fetchall()
    return grades
