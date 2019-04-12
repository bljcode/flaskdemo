import logging
import logging.config
from SafeFileHandler import TimedRotatingFileHandler as newTRFileHandler
import logging.handlers
from config import config

#增加一个判断目录存在与否的函数，原本的得先有目录
def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path
#使用如下
#log_dir_name = "logs"
#log_file_name = 'logger-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
#当前目录上层
#log_file_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + os.sep + log_dir_name
#make_dir(log_file_folder)

applog = logging.getLogger("app")
file = config['default'].LOGPATH + 'strategy-gate.log'
handler = None
#debug模式下，flask开多一个线程来监视项目的变化,所以导致PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问。关掉debug(项目更改不能自动重启)
if config['default'].DEBUG == True:
    handler = logging.FileHandler(file, encoding='UTF-8')
else:
    handler = logging.handlers.TimedRotatingFileHandler(file, when='D', interval=1, backupCount=10,encoding='UTF-8')
    handler.suffix = "%Y-%m-%d.log"
logging_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
applog.addHandler(handler)
applog.setLevel(logging.INFO)


def getMainLog():
    return applog

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
    handler = logging.FileHandler('log\\' + name + '-record.log', encoding='UTF-8')
    logging_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

ai_logger = getLogger("ai")
