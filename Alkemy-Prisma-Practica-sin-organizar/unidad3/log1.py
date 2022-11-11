import logging


#crear log
log = logging.getLogger(__name__) 

#Ajuste de nivel de severidad
log.setLevel(logging.WARNING)

#handlers
p_handlers = logging.StreamHandler()
s_handlers = logging.FileHandler('log1.log')

#Ajustamos los niveles de severidad para cada handlers
p_handlers.setLevel(logging.WARNING)
s_handlers.setLevel(logging.ERROR)

#Ajustamos los formatos para cada handlers
p_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
s_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

#Aplicamos estos formatos a nuestros handlers
p_handlers.setFormatter(p_format)
s_handlers.setFormatter(s_format)

#Agregamos los handlers al logger
log.addHandler(p_handlers)
log.addHandler(s_handlers)

#Probamos el logger

log.warning('Advertencia')
log.error('Error!')

