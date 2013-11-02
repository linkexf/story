__author__ = 'damlin'
#coding=utf-8
from flask import g
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import required, email, equal_to, ValidationError
from flask.ext.babel import gettext, lazy_gettext as _
from .validators import is_username
from models import User
from exts.common import hash_str


class LoginForm(Form):
    name = TextField(_('User Name:'), validators=[required(message=_('请输入用户名!'))])
    password = PasswordField(_('Password:'), validators=[required(message=_('请输入密码!'))])


class SignupForm(Form):
    name = TextField(_("User Name"), validators=[
        required(message=_("User Name required")), is_username])
    email = TextField(_("Email"), validators=[
        required(message=_("Email address required")),
        email(message=_("A valid email address is required"))
    ])
    password = PasswordField(_('Password:'), validators=[required(message=_('请输入密码!'))])

    def validate_name(self, field):
        user = User.query.filter_by(name=field.data and field.data.strip()).first()
        if user:
            raise ValidationError, gettext("This name is taken")

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data and field.data.strip()).first()
        if user:
            raise ValidationError, gettext("This email is taken")


class ChangePasswordForm(Form):
    password_old = PasswordField(_('Old Password:'), validators=[required(message=_('请输入密码!'))])
    password = PasswordField(_('New Password:'), validators=[required(message=_('请输入新密码!'))])
    password_again = PasswordField(_("Password again"), validators=[equal_to("password", message=_("请和新密码保持一致!"))])

    def validate_password_old(self, field):
        if g.user is None or g.user.password != hash_str(field.data):
            raise ValidationError, gettext("当前密码输入错误!")
