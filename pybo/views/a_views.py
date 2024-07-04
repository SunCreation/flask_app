from datetime import datetime
from flask import Blueprint, url_for, request, g
from werkzeug.utils import redirect
from pybo import db
from pybo.models import Question, Answer
import functools
from .auth_views import login_required

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
@login_required
def create(question_id):
    question = Question.query.get_or_404(question_id)
    content = request.form['content']
    answer = Answer(content=content, create_date=datetime.now(), user=g.user)
    question.answer_set.append(answer)
    db.session.commit()
    return redirect(url_for('question.detail', q_id=question_id))


