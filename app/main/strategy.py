from flask import render_template, session, redirect, url_for,request
from . import main
from ..models import example
import json
from app.models.mysql import algorithm_args_dao
from app.models.mysql.domain import algorithm_args


@main.route('/strategy', methods=['GET', 'POST'])
def strategy():
    re = example.importtest("fan")
    return 'in strategy!' + re

@main.route('/args', methods=['GET', 'POST'])
def args():
    args = algorithm_args_dao.selectAll()
    return render_template("args/args.html", args =args)
#两种传参，对应前端两种,通过http请求,看是获取form中参数还是paramter
#ajax传入form形式，返回json形式，因为前端指定，如果返回json格式错误，就进入前端error形式
"""
request.form.get("key", type=str, default=None) 获取表单数据
request.args.get("key") 获取get请求参数
request.values.get("key") 获取所有参数
"""
@main.route('/args/add', methods=['POST'])
def addargs():
    mark = request.form.get('mark', '')
    args = request.form.get('args', '')
    url = request.form.get('url', '')
    print("in addargs,mark")
    t = algorithm_args.Algorithm_Args(mark=mark,args=args,url=url)
    algorithm_args_dao.addOne(t)
    return json.dumps("ok")

@main.route('/args/del', methods=['POST'])
def delargs():
    id = request.form.get('id', None)
    algorithm_args_dao.delete(id)
    return json.dumps("ok")
#window.location.href = "/args/edit/" + id;
@main.route('/args/edit/<id>', methods=['GET','POST'])
def editargs(id):
    print("in edit ,id:" + str(id))
    arg = algorithm_args_dao.selectById(id)
    return render_template("args/argsedit.html", arg =arg)
@main.route('/args/save', methods=['GET','POST'])
def saveargs():
    id = request.form.get('id', None)
    mark = request.form.get('mark', '')
    args = request.form.get('args', '')
    url = request.form.get('url', '')
    arg = algorithm_args_dao.updateById(id,mark,args,url)
    return json.dumps("ok")


if __name__ == '__main__':
    pass
