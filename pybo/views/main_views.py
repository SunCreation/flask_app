from flask import Blueprint, render_template, url_for, session
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    print(session)
    return redirect(url_for('question._list'))


