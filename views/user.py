__author__ = 'damlin'
#coding=utf-8

from flask import g, Blueprint, render_template, request, current_app, redirect, url_for
from flask.ext.principal import identity_changed, Identity, AnonymousIdentity
from models import User
from forms import LoginForm, SignupForm, ChangePasswordForm
from exts import photos
from exts.permissions import auth
from exts.common import hash_str

user = Blueprint('user', __name__)


@user.route('/<name>/')
def index(name):
    user = User.query.filter_by(name=name and name.strip()).first()
    if user:
        return render_template('user/index.html', user=user)
    return redirect(url_for('home.index'))


@user.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user, authenticated = User.query.authenticate(form.name.data, form.password.data)
        if user and authenticated:
            identity_changed.send(current_app._get_current_object(),
                                  identity=Identity(user.pk))
            return redirect('/user')
    return render_template('login.html', form=form)


@user.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if request.method == "POST" and form.validate():
        user = User()
        form.populate_obj(user)
        user.password = hash_str(form.password.data)
        user.save()
        return redirect('/user')
    return render_template('signup.html', form=form)


@user.route("/logout/")
def logout():
    identity_changed.send(current_app._get_current_object(),
                          identity=AnonymousIdentity())
    return redirect('/')


@user.route("/settings/", methods=['GET', 'POST'])
@auth.require(401)
def settings():
    form = ChangePasswordForm(request.form)
    return render_template('user/settings.html', form=form)


@user.route("/settings/password", methods=['POST'])
@auth.require(401)
def change_password():
    form = ChangePasswordForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(name=g.user.name).first()
        user.password = hash_str(form.password.data)
        user.save()
        return redirect(url_for('user.settings'))
    return redirect(url_for('user.settings'))


@user.route("/upload/", methods=['POST'])
@auth.require(401)
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        user = User.query.filter_by(name=g.user.name).first()
        user.photo = photos.url(filename)
        user.save()
    return redirect(url_for('user.settings'))