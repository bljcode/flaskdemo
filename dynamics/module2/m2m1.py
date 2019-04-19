import sys

class M2m1:
    def __init__(self):
        logInfo(str(self.__class__) + " init")
        pass

    def execute(self,parameters):
        print("M2m1 get the input parameter:" + parameters)
        print("Merchan1 model1 start run")
        return "info"


def logInfo(info):
    if 'logger' in sys.modules.keys():
        from logger import doLog
        doLog(str(info))
    else:
        print(str(info))