#config about
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'strategy gate'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    #实现调试前端页面不用重启
    USE_RELOADER = True
    #sql url on test

class ProductionConfig(Config):
    #sql url online
    DEBUG = False
    pass

config = {
    'development': DevelopmentConfig,
    'production' : ProductionConfig,
    'default' : DevelopmentConfig
}