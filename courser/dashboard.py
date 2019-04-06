from flask import (
    Blueprint, render_template, g
)

from werkzeug.exceptions import abort

from .db import query_db, get_db
from .auth import login_required


dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
def index():
    return render_template('dashboard/index.html')
