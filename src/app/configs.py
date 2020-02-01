import os


class DefaultConfig:
    DEBUG: str = 'False'

    SQLALCHEMY_ECHO: bool = False
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


class DevelopmentConfig(DefaultConfig):
    DEBUG: str = os.environ.get('FLASK_DEBUG')

    SQLALCHEMY_ECHO: bool = os.environ.get('FLASK_DEBUG') == 'True'
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


class TestingConfig(DefaultConfig):
    DEBUG: str = 'True'
    TESTING: bool = True

    SQLALCHEMY_ECHO: bool = False
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('DATABASE_URL') + '_testing'
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
