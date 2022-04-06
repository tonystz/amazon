import logging
import logging.handlers
import urllib3
import os

urllib3.disable_warnings()
logger = logging.getLogger()
# from http.client import HTTPConnection
# HTTPConnection.debuglevel = 1

SAVE_BODY = True
def set_debug():
    formatter_str = '%(asctime)s %(levelname)-8s[%(lineno)d:%(filename)s:%(funcName)s()] %(message)s'
    formatter = logging.Formatter(formatter_str)
    logger.setLevel(logging.DEBUG)
    
    try:
        os.mkdir('log')
    except:
        pass

    fh = logging.handlers.RotatingFileHandler(f'log/cr.log',maxBytes=10*1024*1024,backupCount=10)
    
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)


    # Stream
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

set_debug()

def save_body(name,rsp):
    if SAVE_BODY:
        rspf=f'log/rsp{name}.html'
        logger.info(f'save {rsp} to file: {rspf}')
        with open(rspf,'w',encoding='utf-8') as f:
            f.write(rsp.text)
