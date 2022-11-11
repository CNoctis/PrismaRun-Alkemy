from asyncio.log import logger
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s', datefmt="%Y-%m-%dT%H:%M:%S%z")
logger = logging.getLogger(__name__)

def word_count(myfile):
    try:
        with open(myfile, 'r') as f:
            file_data = f.read()
            words = file_data.split(" ")
            final_word_count = len(words)
            logger.info(f"this file has {final_word_count} words")
            return final_word_count
    except OSError as e:
        logger.error("error reading the file")