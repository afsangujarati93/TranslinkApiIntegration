# -*- coding: utf-8 -*-
import logging

class Log_Handler:
    def log_initializer():
        logger = logging.getLogger(__name__)
        if not getattr(logger, 'handler_set', None):
            hdlr = logging.FileHandler('myapp.log')
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            hdlr.setFormatter(formatter)
            logger.addHandler(hdlr) 
            logger.setLevel(logging.DEBUG)
    #        logger = logging.getLogger(__name__)
            logger.propagate = False
            logger.handler_set = True
        return logger
    