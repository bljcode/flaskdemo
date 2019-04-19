

import os
#from logger import doLog
import sys

class M1m1:
    def __init__(self):
        logInfo(str(self.__class__) + " init")

    #一个默认的调用方法
    def execute(self,parameters):
        print("M1m1 get the input parameter:" + parameters)
        print("Merchan1 model1 start run")
        return "info"



#提供一个日志工具
def logInfo(info):
    if 'logger' in sys.modules.keys():
        from logger import doLog
        doLog(str(info))
    else:
        print(str(info))