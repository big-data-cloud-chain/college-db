from flask import (
    Blueprint, render_template, g
)


dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
def home():
    return render_template('dashboard/index.html')
