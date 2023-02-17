# Used for application config.
import sys


class Config(object):
    TESTING = False
    _IS_DEVELOPMENT = False

    def register_all_api(self):
        pass

    @staticmethod
    def is_development_config():
        return 'debug' in sys.argv[1]


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DATABASE_URI = 'mysql://user@localhost'
    DEVELOPMENT = True

