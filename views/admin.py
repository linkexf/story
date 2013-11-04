__author__ = 'damlin'
#coding=utf-8


from flask import Blueprint, render_template


admin = Blueprint('admin', __name__)


@admin.route('/admin')
def index():
    return render_template('admin/index.html')


@admin.route('/admin/new')
def new():
    return render_template('admin/new.html')