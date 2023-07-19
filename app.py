from motherboard.logger import logging
from motherboard.exception import AppException
import sys

logging.info("welcome to cusrtom logging")


try:
    a=4/"6"

except Exception as e:
    raise AppException(e, sys)