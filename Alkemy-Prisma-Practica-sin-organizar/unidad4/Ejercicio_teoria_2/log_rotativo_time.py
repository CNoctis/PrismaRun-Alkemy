from asyncio.log import logger
from cgitb import handler
import logging
from logging.handlers import TimedRotatingFileHandler

# Creamos el logger
logger = logging.getLogger('simple_logger')

# Establecemos el nivel de severidad
logger.setLevel(logging.DEBUG)

# Creamos un time rotating file handler y seteamos el nivel de severidad en debug
handler = TimedRotatingFileHandler('Time_Log_test.log', when='S', interval=2, backupCount=10)
handler.setLevel(logging.DEBUG)

#Creamos un objeto de formato
formatter = logging.Formatter('%asctime)s -%(name)s - %(levelname)s - %(message)s')

#Agregamos el objeto formato rotating file handler
handler.setFormatter(formatter)

#Agregamos el handler al logger
logger.addHandler(handler)

#Generamos los logs
for i in range(20):
    logger.debug(f'debug message{i}')
    logger.info(f'info message{i}')
    logger.warning(f'warn mensaje{i}')
    logger.error(f'error message{i}')
    logger.critical(f'critical message{i}')