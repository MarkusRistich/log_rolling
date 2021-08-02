""" Step 1: explore the various ways that messages can be sent to loggers, and the various logging levels.
"""

# interpreter packages
import logging


def log_no_tracking():
    """ Logging does not require an instance of a logger. A default logger is always running.
    """

    logging.info("Everything looks pretty good!")

    logging.debug("I'm here to be responsible.")

    logging.warning("I'm going to try to recover from this.")

    logging.critical("Fly, you fools!")


def log_from_namedlogger(log):
    """ Use provided logger(logging.Logger) to attach to various levels of logging process.
    """

    log.info("{} : Everything looks pretty good!".format(log.name))

    log.debug("{} : I'm here to be responsible.".format(log.name))

    log.warning("{} : I'm going to try to recover from this.".format(log.name))

    log.critical("{} : Fly, you fools!".format(log.name))


def set_logging_level(log, level):
    """  Logging has a varieties of levels of severity:

    Preventative information:
    -- DEBUG   : Detailed information, typically of interest only when diagnosing problems.
    -- INFO    : Confirmation that things are working as expected.
    -- WARNING : Something unexpected happened, or indicative of some problem in the near future. (Default Level)

    Active information:
    -- ERROR   :  The program has not been able to perform some function, with unknown consequences.
    -- CRITICAL: The program itself may be unable to continue running or imminently at risk of crash.
    """
    logging.basicConfig()
    log.setLevel(level)


def create_logger(name):
    """ Examples of the various logging severity.

    """
    return logging.getLogger(name)


if __name__ == "__main__":
    # log_no_tracking()

    # log = create_logger("")
    # log_from_namedlogger(log)

    local_logger = create_logger(__name__)
    set_logging_level(local_logger, logging.DEBUG)
    log_from_namedlogger(local_logger)

    # shared_logger = create_logger("shared_logger")
    # log_from_namedlogger(shared_logger)