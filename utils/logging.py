import logging
import sys


def config_logger(log_name):
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
    sh = logging.StreamHandler(sys.stdout)  # saida padrao
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    return logger
