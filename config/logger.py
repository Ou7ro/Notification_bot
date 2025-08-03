import logging
import sys


def setup_logger():
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s - %(message)s',
                        datefmt='%H:%M:%S',
                        stream=sys.stdout)
    return logging.getLogger(__name__)


logger = setup_logger()
