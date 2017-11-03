# -*- coding: utf-8 -*-
import logging

class Log_Handler:
    def log_initializer():
        logger = logging.getLogger(__name__)
        hdlr = logging.FileHandler('myapp.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr) 
        logger.setLevel(logging.DEBUG)
        log = logging.getLogger(__name__)
        return logger
    