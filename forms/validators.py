__author__ = 'damlin'
#coding=utf-8

from wtforms.validators import regexp
from flask.ext.babel import lazy_gettext as _

is_username = regexp(r'^\w+$', message=_("You can only use a-z,A-Z,0-9,_"))