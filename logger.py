import logging
import logging.config
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