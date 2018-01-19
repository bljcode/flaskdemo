from flask import render_template, session, redirect, url_for,request,jsonify

from app.models.mysql import algorithm_args_dao
from . import main
import json

@main.route('getlog', methods=['GET', 'POST'])
def db():
    logId = request.form.get('logId', None)
    # dbtest
    re = algorithm_args_dao.selectById(logId)
    #json直接转re不行，将re直接转字典然后转json也不行(因为字典有个**instance字段)，后来就手动转,orm映射的时间是个datetime对象，这里str一下，否则也报can't json
    dict1 = {'id':re.id,'model_name':re.model_name,'code':re.code,'info_data':re.info_data,
             'comment':re.comment,'stop':re.stop,'yn':re.yn,'create_time':str(re.create_time),'end_time':str(re.end_time),
             'mod_time':str(re.mod_time)}
    return  json.dumps(dict1)
    #前端传来的json串 转 字典
    #args = request.form.get('args', '')
    # parameters = json.loads(args)


if __name__ == '__main__':
    pass