from Logger import Logger

LOG_FILE = "/home/swils024/Documents/ansible/roles/common/logs/test.log"

if __name__=="__main__":
    log = Logger(LOG_FILE, level="info")
    log.logger.info("Complete")