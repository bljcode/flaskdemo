from flask import render_template, session, redirect, url_for
from . import main
from logger import ai_logger

@main.route('/', methods=['GET', 'POST'])
def hello_world():
    ai_logger.info("test log info")
    return 'Welcome Here!'


if __name__ == '__main__':
    pass
