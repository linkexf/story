__author__ = 'damlin'
import hashlib


def hash_str(data):
    return  hashlib.md5(data).hexdigest()