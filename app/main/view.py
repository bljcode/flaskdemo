from flask import render_template, session, redirect, url_for
from . import main
from logger import ai_logger
from app.models.mysql import algorithm_args_dao

@main.route('/', methods=['GET', 'POST'])
def hello_world():
    ai_logger.info("test log info")
    return render_template("index.html")
@main.route('/home', methods=['GET', 'POST'])
def hello_world2():
    ai_logger.info("test log info")
    return render_template("index.html")



@main.route('/home', methods=['GET', 'POST'])
def home():
    #args = algorithm_args_dao.selectAll()
    list1 = ['Google', 'Runoob', 1997, 2000];
    return render_template("index.html",args =list1)


if __name__ == '__main__':
    pass
