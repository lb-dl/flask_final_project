import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    TESTING = False
    _IS_DEVELOPMENT = False

    @staticmethod
    def is_development_config():
        return 'debug' in sys.argv[1]


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://admin:password@localhost:3306/easy_learn'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEVELOPMENT = True

