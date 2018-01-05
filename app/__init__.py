from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from config import config
import os

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    #register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #bootstrap init
    bootstrap.init_app(app)

    return app

app = create_app(os.getenv('STRATEGY_CONFIG') or 'default')