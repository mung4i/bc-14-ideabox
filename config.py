<<<<<<< HEAD
# Enable debugging features
DEBUG = True


=======
#Enable debugging features
DEBUG = True

>>>>>>> b55bd1732826a6919470cb2ebc5c73e9d9081570
class Config(object):
    """
    My configs
    """

<<<<<<< HEAD

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
=======
class DevelopmentConfig(Config):
    """
    Dev configs
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """Production configs"""
>>>>>>> b55bd1732826a6919470cb2ebc5c73e9d9081570
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
