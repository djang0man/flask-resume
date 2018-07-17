import os

class DevelopmentConfig(object):
    DATABASE_URI = os.environ["RESUME_DATABASE_URL"]
    DEBUG = True
