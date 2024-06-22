from Logger import Logger

LOG_FILE = "test.log"

if __name__=="__main__":
    log = Logger(LOG_FILE, level="info")
    log.logger.info("Complete")