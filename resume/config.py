import os

class DevelopmentConfig(object):
    DATABASE_URI = os.environ["DATABASE_URL"]
    DEBUG = True
