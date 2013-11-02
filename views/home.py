__author__ = 'damlin'
#coding=utf-8

from flask import Blueprint, render_template


home = Blueprint('home', __name__)


@home.route('/')
def index():
    return render_template('index.html')
