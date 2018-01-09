from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
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

    # nav
    nav = Nav()
    nav.register_element('top', Navbar(u'flaskDemo',
                                       View(u'主页', 'main.hello_world'),
                                       View(u'关于', 'main.hello_world'),
                                       Subgroup(u'项目',
                                                View(u'项目一', 'main.hello_world'),
                                                Separator(),
                                                View(u'项目二', 'main.hello_world2'),
                                                ),
                                       ))
    nav.init_app(app)
    # bootstrap init
    bootstrap.init_app(app)

    return app

app = create_app(os.getenv('STRATEGY_CONFIG') or 'default')