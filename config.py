__author__ = 'damlin'
#coding=utf-8
import os

DEBUG = True
SECRET_KEY = 'secret test'
SECURITY_REGISTERABLE = True

#database#
MYSQL_USER = 'root'
MYSQL_PASS = 'root'
MYSQL_HOST_M = '127.0.0.1'
MYSQL_HOST_S = '127.0.0.1'
MYSQL_PORT = '3306'
MYSQL_DB = 'story'

SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s?charset=utf8' % (MYSQL_USER, MYSQL_PASS, MYSQL_HOST_M, MYSQL_PORT, MYSQL_DB)

MONGOALCHEMY_DATABASE = 'story'
# MONGOALCHEMY_SERVER = '127.0.0.1'
# MONGOALCHEMY_PORT = '27017'

CACHE_TYPE = "simple"
CACHE_DEFAULT_TIMEOUT = 300

UPLOADS_DEFAULT_DEST = os.path.join(os.path.dirname(__file__), 'static')
UPLOADS_DEFAULT_URL = '/static'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = DEBUG
MAIL_USERNAME = 'username'
MAIL_PASSWORD = 'password'
DEFAULT_MAIL_SENDER = 'yourname@domain.com'