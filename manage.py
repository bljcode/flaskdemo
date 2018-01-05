#!/usr/bin/env python

#creat app
from app import app
from flask_script import Manager,Shell

manager = Manager(app)
#parameter: runserver
if __name__ == '__main__':
    manager.run()