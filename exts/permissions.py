__author__ = 'damlin'
#coding=utf-8
from flask.ext.principal import RoleNeed, Permission

admin = Permission(RoleNeed('admin'))
auth = Permission(RoleNeed('auth'))

# this is assigned when you want to block a permission to all
# never assign this role to anyone !
null = Permission(RoleNeed('null'))