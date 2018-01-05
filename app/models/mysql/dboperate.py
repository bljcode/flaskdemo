from app.models.mysql import session,engine
#need pymysql
import pymysql

def select():
    #engine commit immdediately
    print (engine.execute('select * from tablename'))
    session.execute('select * from tablename')
    #session need commit and close
    session.commit()
    # 关闭session:
    session.close()

def insert(modlename,comment):
    #an example to append arguments,\ use to change '
    query = 'INSERT tablename (MODEL_NAME,CODE,INFO_DATA,COMMENT,CREATE_TIME) VALUES (\'%s\',\'1\',\'start\',\'%s\',NOW())' % (
    modlename, comment)
    re = engine.execute(query)
    #查看返回对像内所有属性及方法，看到了laostrowid
    print(dir(re))
    print(re.lastrowid)
    return re.lastrowid



def updateInfo(id,code,info):
    sql = 'UPDATE tablename SET INFO_DATA=CONCAT(INFO_DATA,\'\',\'\\n%s\'),CODE=\'%s\' WHERE ID = %s '%(info,code,id)
    engine.execute(sql)