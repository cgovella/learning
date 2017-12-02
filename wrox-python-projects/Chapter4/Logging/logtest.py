import logging
logging.basicConfig(filename="./log.data", datefmt="%y/%m/%d",
                    format="%(levelname)s: %(asctime)s : %(message)s")
logging.info('Info only')
logging.error('Oops, thats not good')
logging.critical("Didn't think so")


