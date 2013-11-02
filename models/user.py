__author__ = 'damlin'
#coding=utf-8
from exts import db
from flask.ext.principal import RoleNeed, UserNeed, Permission
from flaskext.mongoalchemy import BaseQuery
from werkzeug import cached_property
from datetime import datetime
from exts.permissions import admin
from exts.common import hash_str

now = datetime.now()


class HashField(db.StringField):
    def set_value(self, instance, value, from_db=False):
        print super(HashField, self).from_db
        if from_db:
            super(HashField, self).set_value(instance, value)
        else:
            super(HashField, self).set_value(instance, str(hash_str(value)))


class UserQuery(BaseQuery):
    def from_identity(self, identity):
        user = self.get(identity.id)
        if user:
            identity.provides.update(user.provides)
        identity.user = user
        return user

    def authenticate(self, name, password):
        user = self.filter(self.type.name == name).first()
        if user:
            authenticated = user.check_password(password)
            print authenticated
        else:
            authenticated = False
        return user, authenticated


class User(db.Document):
    query_class = UserQuery
    AUTH, ADMIN = 100, 200
    name = db.StringField()
    email = db.StringField()
    password = db.StringField()
    photo = db.StringField(default='')
    following_count = db.IntField(default=0)
    follower_count = db.IntField(default=0)
    post_count = db.IntField(default=0)
    active = db.BoolField(default=True)
    role = db.EnumField(db.IntField(), AUTH, ADMIN, default=AUTH)

    @db.computed_field(db.DateTimeField())
    def updated(self):
        return now

    @property
    def created_time(self):
        if self.has_id():
            return self.mongo_id.generation_time

    def check_password(self, password):
        if self.password is None:
            return False
        return self.password == hash_str(password)

    class Permissions(object):
        def __init__(self, obj):
            self.obj = obj

        @cached_property
        def edit(self):
            return Permission(UserNeed(self.obj.pk)) & admin

        @cached_property
        def delete(self):
            return Permission(UserNeed(self.obj.pk)) & admin

    @cached_property
    def pk(self):
        return str(self.mongo_id)

    @cached_property
    def permissions(self):
        return self.Permissions(self)

    @cached_property
    def provides(self):
        needs = [RoleNeed('auth'), UserNeed(self.pk)]
        if self.is_admin:
            needs.append(RoleNeed('admin'))
        return needs

    @property
    def is_admin(self):
        return self.role >= self.ADMIN
