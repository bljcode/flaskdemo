import sys



#可用来提供对外模板时，提供日志工具,如果执行py的环境中没有导入项目中的logger，就pint
#具体可见module_dynamic中
def logInfo(info):
    if 'logger' in sys.modules.keys():
        from logger import doLog
        doLog(str(info))
    else:
        print(str(info))


if __name__ == '__main__':
    pass
