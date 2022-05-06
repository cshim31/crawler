import logging

logging.basicConfig(filename='std.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def log_debug(str):
    logger.debug(str)

def log_info(str):
    logger.info(str)

def log_warning(str):
    logger.warning(str)

def log_error(str):
    logger.error(str)

def log_critical(str):
    logger.critical(str)