# 导入:
from sqlalchemy import Column,String,Date,Integer,BigInteger,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# 创建对象的基类:
Base = declarative_base()

#the table object
class Algorithm_Args(Base):
    #表名
    __tablename__ = 'py_algorithm_args'

    #列
    id = Column(BigInteger,primary_key=True)
    mark = Column(String)
    args = Column(String)
    create_time = Column(Date,default=datetime.now())
    mod_time = Column(Date)
    yn = Column(Integer,default=1)



