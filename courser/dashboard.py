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
    return render_template('dashboard/enroll.html', course=course, teacher=teacher)


@dashboard.route('/grades')
@login_required
def grades():
    user_id = g.user['id']
    grade_cursor = get_db().execute(
        'SELECT c.title, e.section_id, e.grade '
        'FROM Enrolment AS e '
        'INNER JOIN Section AS s '
        'ON e.section_id = s.id '
        'INNER JOIN Course AS c '
        'ON c.id = s.course_id '
        'WHERE e.student_id = ?'
        , [user_id]
    )
    return render_template('dashboard/grades.html', grades=grade_cursor.fetchall())


@dashboard.route('/')
@login_required
def index():
    return render_template('dashboard/index.html')


def get_grades(id):
    grades = get_db().execute(
        'SELECT co.title, en.grade FROM Enrolment AS en '
        'INNER JOIN Section AS sec '
        'ON en.section_id = sec.id '
        'INNER JOIN Course AS co '
        'ON sec.course_id = co.id '
        'WHERE en.student_id=? ', (id,)
    ).fetchall()
    return grades
