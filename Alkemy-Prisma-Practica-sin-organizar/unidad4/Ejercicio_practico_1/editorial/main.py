import logging
from logging import config

# We specify the working path since logging works from the root not where the .py file is executed
log_file_path = "./config/log_cofing.conf"
logging.config.fileConfig(log_file_path)

logger = logging.getLogger('main')

if __name__ == '__main__':
   logger.INFO('This is an information message')