import os, random, string

class Config(object):
    CSRF_ENABLE = True
    SECRET = '9c9dcd702fc6df1964e6c44b544c9f058987af9893c9ebc8c611f7bc34c898b4'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://tst_edson:Pass@123@localhost:3306/db_flask_mvc'


app_config = {
    'development': DevelopmentConfig(),
    'Testing': None,
    'production': None   
}

app_active = os.getenv('FLASK_ENV')

if app_config is None:
    app_config = 'development'
        
