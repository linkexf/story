__author__ = 'damlin'

from flask.ext.mail import Mail
from flaskext.mongoalchemy import MongoAlchemy
from flaskext.uploads import UploadSet, IMAGES


__all__ = ['mail', 'db', 'photos']

mail = Mail()
db = MongoAlchemy()
photos = UploadSet('photos', IMAGES)
