#!/usr/bin/env python
import os
#creat app
from app import create_app
from flask_script import Manager,Shell

app = create_app(os.getenv('STRATEGY_CONFIG') or 'default')
manager = Manager(app)
#parameter: runserver
if __name__ == '__main__':
    manager.run()