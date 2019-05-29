#更改使用方式，原本logger形式，出现多模块时不打日志，又发现文件配置比较简洁，就切换了logUtil.py
import logUtil
from config import config,DevelopmentConfig,ProductionConfig
applog= logUtil.getLogger()
#这个主要是为了模型本地测试
def doLog(info):
    if config["default"].DEBUG:
        #applog.info(info)
        print(str(info))
    else:
        applog.info(info)


def getLogger():
    return applog



if __name__ == '__main__':
    try:
        a = 3/0
    except Exception as e:
        applog.error('Got an error ',exc_info=True)
    getLogger().info("test")
    #ai_logger.info("test")