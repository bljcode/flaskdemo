import logging
import os
import logging.config

def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path

conf_path = 'conf/logging.ini'
logging.config.fileConfig(conf_path)
#当前目录上层
log_dir_name = "logs"
log_file_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + os.sep + log_dir_name
make_dir(log_file_folder)

#关掉werkzeug日志
werkzeuglogger = logging.getLogger('werkzeug')
werkzeuglogger.setLevel(logging.ERROR)
werkzeuglogger.disabled = True


def getLogger():
    #默认返回fan的日志记录器
    return logging.getLogger('fan')


if __name__ == '__main__':
    try:
        a = 3/0
    except Exception as e:
        logging.error('Got an error ',exc_info=True)
