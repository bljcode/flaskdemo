from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#python3 is diff from python2
import urllib.parse

#this way to avoid spe char in password like @
DB_CONNECT_STRING = 'mysql+pymysql://user:%s@172.25.28.5:3306/consumeranalysis_tag?charset=utf8'% urllib.parse.unquote('password')
#"mysql+mysqldb://root:%s@127.0.0.1:3306/dbname?charset=utf8" % urlquote('password')
engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()