#Enable debugging features
DEBUG = True

class Config(object):
    """
    My configs
    """

class DevelopmentConfig(Config):
    """
    Dev configs
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """Production configs"""
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
