from flask import Blueprint, render_template
webRoutes = Blueprint('web', __name__)


@webRoutes.route('/')
def index():
    return render_template('user/create.html', name='he')
