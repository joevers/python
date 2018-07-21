import logging

LOG_FORMAT = "%(asctime)s=====%(levelname)s+++++%(message)s"

logging.basicConfig(filename="tulingxueyuan.log", level=logging.DEBUG, format=LOG_FORMAT)

logging.log(logging.DEBUG, "This is a debug log")
logging.log(logging.WARNING, "This is a warning log")
