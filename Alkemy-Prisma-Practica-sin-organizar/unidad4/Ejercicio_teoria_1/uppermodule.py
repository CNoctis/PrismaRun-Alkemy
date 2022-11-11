import logging
import lowermodule

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s', datefmt="%Y-%m-%dT%H:%M:%S%z")
logger = logging.getLogger(__name__)

def record_words_count(myfile):
    logger.info("starting the function")
    try:
        words_count = lowermodule.word_count(myfile)
        with open('wordcountarchive.csv', 'a') as file:
            row = str(myfile) + ',' + str(words_count)
            file.write(row + '\n')
    except:
        logger.warning(f"could not write file {myfile} to destination")

    finally:
        logger.debug(f"the function is done for the file {myfile}")
def main():
    record_words_count('texto_prueba.txt')

if __name__ == '__main__':
    main()