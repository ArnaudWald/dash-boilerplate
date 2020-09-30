# -*- coding: utf-8 -*-
"""Job script."""
import coloredlogs
from concurrent.futures import TimeoutError
import logging
from pebble import concurrent, ProcessExpired
import time

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO',
                    fmt='%(asctime)s %(name)s %(levelname)s %(message)s')

TIMEOUT = 100  # seconds


@concurrent.process(timeout=TIMEOUT)
def job2_with_timeout(some_arg):
    """Do something."""
    logging.info('Job started.')
    t_start = time.time()

    # Your code here
    time.sleep(5)
    logging.info(some_arg)
    time.sleep(5)

    logging.info("Job completed successfully. Took %05.02fs" % (time.time() - t_start))
    return True


def job2():
    """Define job spec."""
    logger.info("Starting...")
    t_zero = time.time()

    job2_future = job2_with_timeout(some_arg="This is Job 2.")

    try:
        _ = job2_future.result()
    except TimeoutError as error:
        logger.warning("Something went wrong while running job: took longer than %d seconds" % error.args[1])
    except ProcessExpired as error:
        logger.warning("%s. Exit code: %d" % (error, error.exitcode))
    except Exception as error:
        logger.warning("Something went wrong while running job: raised %s" % error)
        logger.warning(error.traceback)  # Python's traceback of remote process

    logger.info("Total time:  %05.02fs" % (time.time() - t_zero))


if __name__ == '__main__':
    job2()
