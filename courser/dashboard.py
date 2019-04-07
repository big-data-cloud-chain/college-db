from flask import (
    Blueprint, render_template, g, redirect, url_for, request, flash, session
)

from werkzeug.exceptions import abort

from .db import query_db, get_db
from .auth import login_required


dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/courses')
@login_required
def courses():
    db = get_db()
    all_courses = db.execute('SELECT * FROM Course')
    # gets the column names so they're not hardcoded in the template
    column_names = [desc[0] for desc in all_courses.description]
    return render_template('dashboard/courses.html', columns=column_names, courses=all_courses.fetchall())


@dashboard.route('/enroll', methods=('GET', 'POST'))
@login_required
def enroll():
    if request.method == 'GET':
        course_id = request.args.get('course_id')
        course = get_db().execute(
            'SELECT c.title '
            'FROM Course AS c '
            'WHERE c.id = ? ', [course_id]
        ).fetchone()
        user_id = session.get('user_id')
        teacher = get_db().execute(
            'SELECT t.name '
            'FROM Teacher AS t '
            'INNER JOIN Section AS s '
            'ON s.teacher_id = t.id AND s.course_id = ? ',
            [course_id]
        ).fetchone()
    # Check if the currently logged in user is already enrolled in the course
    return render_template('dashboard/enroll.html', course=course, teacher=teacher)


@dashboard.route('/')
@login_required
def index():
    grades = get_grades(session['user_id'])
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
