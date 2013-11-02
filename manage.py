__author__ = 'damlin'
#coding=utf-8

from flask.ext.script import Server,  Manager
from story import create_app
import config

manager = Manager(create_app(config))

manager.add_command("runserver", Server('0.0.0.0', port=8080))


if __name__ == "__main__":
    manager.run()