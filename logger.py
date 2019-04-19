import logging
import logging.config
from SafeFileHandler import TimedRotatingFileHandler as newTRFileHandler
import logging.handlers
from config import config,DevelopmentConfig
import os
import time

def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path


log_dir_name = "logs"
log_file_name = 'logger-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
#当前目录上层
log_file_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + os.sep + log_dir_name
make_dir(log_file_folder)
applog = logging.getLogger("app")
file = log_file_folder + os.sep + log_file_name
handler = None
#logging.handlers.TimedRotatingFileHandler;
#debug模式下，flask开多一个线程来监视项目的变化,所以导致PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问。关掉debug(项目更改不能自动重启)
if config['default'].DEBUG == True:
    handler = logging.FileHandler(file, encoding='UTF-8')
else:
    handler = logging.handlers.TimedRotatingFileHandler(file, when='S', interval=1, backupCount=10,encoding='UTF-8')
    handler.suffix = "%Y-%m-%d_%H-%M-%S.log"
logging_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
applog.addHandler(handler)
applog.setLevel(logging.INFO)


def getMainLog():
    return applog
#直接打印日志，如果测试的话
def doLog(info):
    if config["default"] is DevelopmentConfig:
        print(str(info))
    else:
       applog.info(info)

#common log
def getLogger(name):
    logger = logging.getLogger(name)
    handler = logging.FileHandler('strategy-gate.log', encoding='UTF-8')
    logging_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

#log for recordProcess
def getRecordLogger(name):
    logger = logging.getLogger(name)
    name_log_file_name = 'logger-' + name + '-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    name_file = log_file_folder + os.sep + name_log_file_name
    name_handler = logging.handlers.TimedRotatingFileHandler(name_file, when='S', interval=1, backupCount=10,
                                                             encoding='UTF-8')
    name_handler.suffix = "%Y-%m-%d_%H-%M-%S.log"
    name_handler.setFormatter(logging_format)
    logger.addHandler(name_handler)
    logger.setLevel(logging.INFO)
    return logger

ai_logger = getLogger("ai")