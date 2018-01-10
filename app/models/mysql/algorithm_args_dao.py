from datetime import datetime

from app.models.mysql.domain.algorithm_args import Algorithm_Args
from app.models.mysql import engine, session


def addOne(al_args):
    session.add(al_args)
    session.commit()
    session.close()

def selectAll():
    users = session.query(Algorithm_Args).filter(Algorithm_Args.yn==1).all()
    return users

def selectByMark(mark):
    user = session.query(Algorithm_Args).filter(Algorithm_Args.mark==mark,Algorithm_Args.yn==1).all()

    return user
def selectById(id):
    user = session.query(Algorithm_Args).filter(Algorithm_Args.id==id,Algorithm_Args.yn==1).one()
    return user
def updateByMark(mark,args):
    session.query(Algorithm_Args).filter(Algorithm_Args.mark==mark).update({"args": args})
    session.commit()
def updateById(id,mark,args,url):
    session.query(Algorithm_Args).filter(Algorithm_Args.id==id).update({"mark":mark,"args": args,"url":url})
    session.commit()
def delete(id):
    session.query(Algorithm_Args).filter(Algorithm_Args.id == id).update({"yn":0})
    session.commit()

#session.query(User).filter(User.id == '5').one()
if __name__ == "__main__":
    t = Algorithm_Args(mark='fan4')
    #delete(5)
    #addOne(t)
    s = updateById(4,'update',None,None)
    print("end")


