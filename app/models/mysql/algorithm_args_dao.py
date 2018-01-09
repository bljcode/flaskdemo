from app.models.mysql import engine,session
from app.models.mysql.domain.algorithm_args import Algorithm_Args
from datetime import datetime

def addOne(al_args):
    session.add(al_args)
    session.commit()
    session.close()
#no commit
def selectAll():
    users = session.query(Algorithm_Args).all()
    return users

def selectByMark(mark):
    user = session.query(Algorithm_Args).filter(Algorithm_Args.mark==mark).all()

    return user
def updateByMark(mark,args):
    session.query(Algorithm_Args).filter(Algorithm_Args.mark==mark).update({"args": args})
    session.commit()

def delete(id):
    session.query(Algorithm_Args).filter(Algorithm_Args.id == 3).delete()
    session.commit()

#session.query(User).filter(User.id == '5').one()
if __name__ == "__main__":
    t = Algorithm_Args(mark='fan3')
    r = selectAll()
    for i in r:
        print(i.mark)
    r2 = selectByMark('fan2')
    for i in r2:
        print("mark:" + i.mark + ",id:" + str(i.id))
    r3 = updateByMark('fan','{json}')