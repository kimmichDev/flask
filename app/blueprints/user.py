from flask import Blueprint, request, render_template, url_for, redirect
from markupsafe import escape
from app.services import userService
userRoutes = Blueprint('user', __name__)


@userRoutes.get('/users')
def index():
    users = userService.getUsers()
    return render_template('user/index.html', users=users)


@userRoutes.route('/users/<int:id>', methods=['get'])
def show(id):
    user = userService.getUser(id=id)
    return render_template('user/detail.html', user=user)


@userRoutes.get('/users/create')
def create():
    return render_template('user/create.html', title='create user')


@userRoutes.post('/users')
def store():
    data = request.form
    userService.create(data=data)
    return redirect(url_for('user.create'))
